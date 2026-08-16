# A Cascade Engine for Odisha Farm Resilience

## 1. EXECUTIVE SUMMARY

- **Model the chain, not the alert**: Odisha's Mahanadi, Brahmani, and Baitarani share a delta where simultaneous floodwaters intermingle, and high tide makes the interaction more acute [5]. The prototype should therefore represent cyclone, rain, river flow, tide, surge, embankment, farm, livelihood, and recovery as one signed, time-indexed graph.
- **Use local events as calibration anchors**: Fani affected **108,220 ha** of annual and perennial crops and caused estimated crop-production losses of **INR 1,304.58 crore** [30]. Yaas produced **130-140 kmph** winds, rainfall of up to **29 cm** at Chandbali, and a **2-4 m** surge over astronomical tide in Balasore and Bhadrak [28]. Replay these two events before attempting live prediction.
- **Keep dependence separate from causation**: IPCC and compound-event literature recognize simultaneous, successive, multivariate, and spatially connected hazards [12][10]. A copula can model dependence among rain, river level, surge, and tide, but it does not prove that one hazard caused another.
- **Do not invent an Odisha Gumbel coefficient**: An Alappuzha study tested Gumbel-Hougaard, Clayton, and Frank copulas for rainfall and water-level rise [33], while a Peninsular India analysis identifies Mahanadi as highly exposed to multivariate flood conditions [9]. Neither retrieved source supplies a validated Odisha coastal surge-rain-river Gumbel parameter that can be copied into production.
- **Bayesian networks are the most defensible core**: BN-FLEMO Delta predicts a distribution of flood loss even when predictors are missing and achieved absolute MAE **0.18 +/- 0.01** and CRPS **0.11 +/- 0.01** [20]. A Pearl River Delta cascade BN exceeded **80%** accuracy, but its authors warn that a static DAG cannot resolve delayed flood peaks or levee failures [13]. Use a dynamic Bayesian network or time-sliced DAG.
- **Quantify crop response only where evidence exists**: A randomized trial across **128 Odisha villages** found that Swarna-Sub1's yield advantage increased by **64 kg/ha per additional flood day**, reaching about **718 kg/ha** under severe submergence [14]. By contrast, the global **32.9%** average waterlogging loss is a prior, not an Odisha rice coefficient [18].
- **Treat salinity as measured state, not a binary flag**: A Sacramento Valley field study estimated a rice threshold of **1.9 dS/m** and a **9.1%** yield decline per dS/m above it [23]. This is useful for the prototype's functional form, but Odisha needs local soil-water EC, variety, growth-stage, and drainage calibration.
- **Reject automatic flood-to-pest claims**: ICAR reports BPH losses of **40-70%**, reaching **70-100%** in severe infestation, and documents repeated Odisha outbreaks [19]. Its decision support uses temperature, humidity, wind, transplanting time, and immigration rather than flood as a direct cause [6]. Flood should modify habitat covariates, not deterministically trigger BPH.
- **Include positive cascades, but distinguish managed systems from accidents**: A managed aquifer-recharge trial stored **26-62 million litres per monsoon** [36]. Managed paddy-fish culture produced about **150 kg fish/ha** [38]. Neither result proves that uncontrolled field flooding or accidental fish ingress raises Odisha paddy yield.
- **Make risk decisions tail-aware**: CVaR is the expected loss beyond the VaR threshold and has a convex, sample-based optimization representation [15]. Compute 95% CVaR at every loss-bearing node, but optimize it only where the system has a real action choice.
- **Deliver an evolving incident, not repeated one-shot texts**: IMD already defines 72-hour watch, 48-hour alert, 24-hour warning, and 12-hour post-landfall outlook stages [22]. CAP supplies Alert, Update, Cancel, Ack, and Error message semantics [24]. The SMS/IVR layer should update one incident record rather than create disconnected advisories.

**Decision-ready insight:** The winning prototype is not a giant universal model. It is a small, auditable dynamic graph calibrated on Fani and Yaas, with explicit uncertainty, local sensor updates, and visible labels separating measured coefficients, transferable priors, and unsupported hypotheses.

## 2. THE CASCADE ARCHITECTURE

### 2.1 Edge semantics

Each edge should have `type`, `sign`, `lag`, `conditional_probability`, `effect_distribution`, `evidence_scope`, `source`, and `calibration_status` fields.

- **TRIGGER**: changes the probability that a downstream state begins.
- **AMPLIFY**: changes the severity or duration of an already possible state.
- **CASCADE**: transmits state, damage, shortage, or recovery downstream.
- **COMPOUND**: joins dependent parents whose combined impact is not represented by independent marginal risks.
- **POSITIVE** is not a fifth causal type. It is `sign=positive` on a TRIGGER, AMPLIFY, or CASCADE edge.

### 2.2 Full typed graph and evidence ledger

| From -> To | Type and sign | Published magnitude or evidence | Engine treatment |
|---|---|---|---|
| Cyclone intensity/track -> damaging wind | TRIGGER, negative | Fani reached **175-185 kmph**, gusting to **205 kmph** near Puri [29]. Yaas reached **130-140 kmph**, gusting to **155 kmph**, over Balasore and Bhadrak [28]. | IMD forecast ensemble -> farm-level wind distribution; condition on distance, track error, exposure, and asset type. |
| Cyclone -> storm surge | TRIGGER, negative | Fani's estimated surge was about **1.5 m** above astronomical tide [29]; Yaas produced **2-4 m** over astronomical tide in Balasore and Bhadrak [28]. | Event-specific surge prior; never infer surge from wind alone when an IMD surge forecast exists. |
| Surge + astronomical tide -> coastal inundation | COMPOUND, negative | IMD explicitly attributes Yaas's higher tidal wave to the combination of full-moon astronomical tide and surge [28]. | Joint parent node using tide as deterministic input and surge as probabilistic input. |
| Cyclone -> extreme rain | TRIGGER, negative or positive | During Yaas, Chandbali received **29 cm**, Rajkanika and Garadapur **25 cm**, and Marsaghai and Kujanga **23 cm** [28]. | Spatial rainfall field, not one district-wide scalar. |
| Rain + antecedent soil moisture -> runoff/river level | COMPOUND, negative | Peninsular India research models precipitation, runoff, and antecedent soil moisture jointly; Mahanadi was the basin most prone to extreme compound scenarios in that study [9]. | Copula or multivariate BN; estimate Odisha parameters from synchronized IMD, gauge, and soil-moisture records. |
| Mahanadi + Brahmani + Baitarani spates -> delta flood | COMPOUND and AMPLIFY, negative | Odisha sources describe a common delta where simultaneous floodwaters intermingle and cause greater havoc [5]. | River nodes remain separate until a confluence/delta interaction node. |
| Delta flood + high tide -> drainage lock | AMPLIFY, negative | The shared-delta flood problem becomes more acute when floods coincide with high tide [5]. | Tide-controlled outfall capacity and delayed recession time. |
| River/surge -> embankment stress or breach -> field | CASCADE, negative | After Yaas, reporting described saline field inundation where rainwater breached embankments [2]. Fani assessment also found embankment stretches requiring restoration [30]. | Separate overtopping, breach, and drainage-failure states; infer breach only from inspection, remote sensing, or water-level discontinuity. |
| Coastal inundation -> field salinity | CASCADE, negative | After Yaas, at least **5,882 ha** in five Balasore blocks and around **1,400 ha** in three Bhadrak blocks were affected; salt deposits created uncertainty over Kharif cultivation [2]. | Update soil-water EC posterior from field sensors and laboratory samples. |
| Field salinity -> rice stress/yield -> next-season suitability | CASCADE, negative | Transferable field response: threshold **1.9 dS/m**, then approximately **9.1%** yield loss per additional dS/m for two California varieties [23]. | Use only as a broad prior; replace with Odisha variety-by-stage response. Carry posterior salinity and leaching into the next-season state. |
| Flood depth + duration + crop stage -> waterlogging stress | COMPOUND, negative | Meta-analysis of **2,419 comparisons from 115 studies** found average yield loss of **32.9%**, with larger losses as duration increased [18]. | Hierarchical prior by crop and stage, widened for transfer uncertainty. |
| Submergence duration + rice variety -> yield | AMPLIFY or mitigate | In Odisha, Swarna-Sub1's advantage rose **64 kg/ha per flood day** and reached about **718 kg/ha** under severe flooding [14]. Without flooding, the estimated **180 kg/ha** disadvantage was not statistically different from zero [14]. | Directly buildable Odisha conditional response; add variety as an action node before sowing. |
| Waterlogging -> root stress/rot | CASCADE, negative | Physiological waterlogging damage is well supported by the meta-analysis, but the retrieved evidence does not provide an Odisha root-rot transition probability [18]. | Include `root_stress`; leave `root_rot` unquantified until field or plant-pathology evidence is collected. |
| Inundation + humid microclimate + susceptible crop -> fungal loss | COMPOUND, negative | Fani's assessment reports fungal attack on mung pods following heavy-rain inundation [30]. | Crop-specific disease node with humidity, leaf wetness, temperature, inoculum, and crop stage as parents. |
| Flood -> rice blast | Proposed COMPOUND, not direct trigger | Rice blast may cause **10-30%** annual yield loss under favorable conditions, and infection begins when conidia attach and germinate [25]. The retrieved source does not show that flood itself causes blast. | Activate scouting probability through wetness and weather covariates; do not issue deterministic spray advice from flood status. |
| Flood -> BPH outbreak | Proposed COMPOUND, not direct trigger | BPH can cause **40-70%** loss and severe infestation **70-100%**, but documented drivers include temperature, humidity, wind, transplant date, and immigration [19][6]. | Use a migration/weather hazard model; add SIR-style spread only after local surveillance data identify susceptible, infested, and managed field states. |
| Crop and stored-input loss -> seed gap | CASCADE, negative | Fani recovery planning called for seeds and seedlings and urgent maintenance of seed supply chains for Kharif and Rabi [30]. | Inventory node: household seed, dealer stock, road access, and expected replenishment date. No loss coefficient is yet available. |
| Seed gap -> delayed/changed sowing -> next-season yield | CASCADE, negative | The existence of an urgent seed-supply problem is documented, but no retrieved Odisha source quantifies days of delay or yield elasticity [30]. | Prototype as a scenario parameter, visibly marked `assumed`, pending dealer and farmer data. |
| Asset/crop loss -> credit need -> debt stress | CASCADE, negative | Fani assessment says collateral requirements can make institutional credit difficult and that some fishers fall back on high-interest private lenders [30]. In a 400-household Bhadrak study, landless farmers lacked crop compensation and loan-waiver access [37]. | Household tenure, outstanding loan, lender, collateral, and compensation eligibility become causal parents. Do not assign an interest-rate or debt coefficient without survey data. |
| Flood/cyclone -> road, cold-chain, mandi disruption -> price | CASCADE, negative | Fani assessment records dependence on middlemen, distress selling of perishable fish, and need for connectivity, cold chain, ice plants, and refrigerated vehicles [30]. | Market-access state modifies farm-gate price distribution and action feasibility; current evidence is qualitative, not an elasticity. |
| Flood shock -> asset sale or migration -> recovery | CASCADE with mixed sign | In **400 households across 40 Bhadrak villages**, labor migration increased the likelihood of economic recovery while selling productive assets reduced it; poorer households faced greater constraints [37]. | Recovery-state transition model stratified by land tenure, wealth, assets sold, migration, compensation, and community support. |
| Excess monsoon flow -> managed recharge -> dry-season water | CASCADE, positive | The Uttar Pradesh UTFI trial diverted excess flow through a pond and 10 recharge wells, storing **26-62 million litres** per monsoon [36]. | Optional intervention node requiring hydrogeologic suitability and water-quality checks; not a default benefit of flooding. |
| Flood sediment -> soil nutrient/health | CASCADE, potentially positive | Vietnam flood-based systems accumulated **229.4-299.2 g/m2** sediment; soil health correlated with sediment mass, but the study lacked crop-yield and economic data [17]. | Record sediment depth and contamination; do not credit yield until local tests distinguish fertile silt from saline or polluted deposits. |
| Managed rice-fish system -> fish output/income | CASCADE, positive | Arunachal guidance reports about **150 kg fish/ha**, with engineered channels, controlled stocking, and managed water [38]. | Model only if the farm is configured for rice-fish culture. Uncontrolled fish ingress remains an unverified hypothesis. |
| Drought precondition -> subsequent flood impact | COMPOUND, sign varies | Compound-event typology supports preconditioned and temporally compounding hazards [10], but no retrieved Odisha coefficient establishes drought as a cause of the next flood. | Drought changes soil, debt, reservoir, and preparedness states; it does not raise flood probability unless data demonstrate that dependence. |

The graph's strongest local quantitative edges are cyclone -> wind/surge/rain, flood duration x variety -> rice yield, and disaster -> crop area/loss. Salinity response, recharge, sediment, and rice-fish values are useful transfer priors, not Odisha production coefficients.

### 2.3 Case study: Fani exposes the difference between hazard and cascade loss

Fani made landfall on **3 May 2019** near Puri as an extremely severe cyclonic storm [30]. It affected **88,486 ha** of annual crops and **19,734 ha** of perennial crops, producing estimated crop losses of **INR 1,304.58 crore** and crop recovery needs of **INR 970 crore** [30]. The assessment also recorded losses to fishing assets, livestock, markets, power, employment, and seed supply, demonstrating that farm impact cannot be reduced to a wind-speed threshold.

The positive operational result is equally important: advance warning enabled evacuation of more than **2 lakh fishers** from seven coastal districts with zero casualties among them [30]. This reveals the intended engine mechanism: forecast skill matters only when it changes a feasible action before the affected node crosses its failure threshold.

### 2.4 Case study: Yaas is the prototype's compound-event test

Yaas supplies a compact Odisha test of wind + rain + surge + tide + embankment + salinity. IMD recorded strong winds, up to **29 cm** rainfall, and a **2-4 m** surge; it also identified a full-moon tide interaction [28]. Subsequent field reporting linked inundation and embankment failure to saline agricultural land and uncertainty about Kharif sowing [2].

A successful replay should not merely reproduce a district damage class. It should show how the surge and tide posterior changes inundation, how a breach observation updates field salinity, and how the salinity posterior changes the advice from "sow" to "test EC, drain or flush, then select a crop."

## 3. THE MATH INVENTORY

| Method: what | Published source, URL, date | What it models | Prototype buildability | Grade |
|---|---|---|---|---|
| Typed, signed, time-sliced causal DAG | BN-FLEMO Delta, https://nhess.copernicus.org/articles/25/2845/2025/, 2025 [20] | Conditional dependencies among hazard, exposure, action, impact, and recovery nodes | High. Implement in NetworkX/pgmpy with evidence metadata and one slice per advisory update | **A** |
| Copulas, including Gumbel-Hougaard | Zscheischler et al., https://doi.org/10.1038/s43017-020-0060-z, 15 Jun 2020 [10]; Alappuzha study, 2023 [33] | Nonlinear joint dependence and return periods for rain, river level, surge, tide, or soil moisture | Medium. Fit only when synchronized records are available. The Alappuzha paper tests Gumbel, Clayton, and Frank, but retrieved text does not expose a reusable Odisha parameter | **B** |
| Bayesian flood-loss network | BN-FLEMO Delta, URL above, 2025 | Probability distribution of damage with missing predictors; uncertainty-aware inference | High. Replace building variables with farm depth, duration, crop, stage, salinity, and action nodes; recalibrate locally | **A** |
| Bayesian cascade network | Zhang et al., https://www.nature.com/articles/s44304-025-00115-1, 2025 [13] | Upstream-to-downstream node failure and critical transmission hubs | Medium-high. Use dynamic slices because static BN structure misses time lags [13] | **B** |
| Cascading-failure criticality | Nedic et al., https://www.sciencedirect.com/science/article/pii/S0142061506000810, 2006 [26] | Threshold behavior: one failure increases load on remaining components, making subsequent failure more likely | Medium. Transfer the load/capacity logic, not power-grid coefficients | **B** |
| Hawkes self-exciting point process | Hawkes Models and Their Applications, https://arxiv.org/html/2405.10527v1, 2024 [11] | Clustering in event arrival times; marked variants can include severity or basin | Technically easy, scientifically conditional. Fit only if event catalogs show residual clustering after seasonality and climate covariates | **C** |
| SIR-style pest spread and blast dispersal | ICAR-NRRI BPH bulletin, date not stated in retrieved copy [19]; rice-blast review, date in source page not recovered [25] | Movement among susceptible, infested, and controlled fields; weather-driven inoculum or vector pressure | Low without geolocated surveillance and intervention data. Generic SIR is demonstrable but not validated for post-flood Odisha BPH | **D** |
| System dynamics and causal-loop diagrams | Enhancing household rice farmers' welfare under climate change conditions, https://iopscience.iop.org/article/10.1088/1755-1315/1323/1/012009, 2024 [16] | Feedback among seed, production, price, income, livelihood assets, adaptation, and credit | Medium for explanation and policy simulation; weak for event-level prediction until stocks, flows, equations, and local parameters are supplied | **C** |
| Monte Carlo uncertainty propagation with convergence gates | Stopping Rules for Monte Carlo Methods: A Review, https://arxiv.org/pdf/2510.22688, 2025 [27] | Propagates joint uncertainty through the graph and estimates expected loss, quantiles, and tail loss | High. Use independent pilot and main stages, fixed-width confidence intervals, and absolute/relative precision gates; do not terminate at an arbitrary sample count [27] | **A** |
| CVaR optimization | Rockafellar and Uryasev, Optimization of Conditional Value-at-Risk, source dated 5 Sep 1999 [15], https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf | Expected loss in the tail beyond VaR; comparison of action choices under severe scenarios | High. Sample formulation is convex and piecewise linear and can be solved with linear programming [15] | **A** |
| Dynamic incident state machine and CAP | IMD four-stage warning system, https://mausam.imd.gov.in/; CAP 1.2, https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html, 1 Jul 2010 [24] | Event identity, lead-time state, updates, cancellations, onset, expiry, acknowledgement, and recovery progression | High. Use IMD phase as external state and farm-impact/recovery as internal state | **A** |

**Grades:** A = directly demonstrable with strong precedent; B = sound but needs local calibration; C = useful exploratory layer with major identification limits; D = filler unless new data are collected.

The key architecture choice is a dynamic BN plus Monte Carlo and CVaR, not an undifferentiated stack of every mathematical method. Copulas model selected joint inputs; system dynamics handles slower livelihood feedback; Hawkes and SIR remain optional research modules.

## 4. COMPOUND EVENT EVIDENCE

Compound events combine multiple drivers or hazards that jointly create significant impact [31]. Zscheischler et al. classify them as preconditioned, multivariate, temporally compounding, and spatially compounding, while warning that class boundaries can overlap [10].

| Compound event | Documented evidence | What can be claimed | What cannot be claimed |
|---|---|---|---|
| Cyclone + wind + rain + surge + tide | Yaas combined **130-140 kmph** wind, up to **29 cm** rain, **2-4 m** surge, and full-moon astronomical tide [28] | A documented multivariate coastal compound event in Odisha | A single published Odisha interaction coefficient |
| Surge + rain + embankment failure + saline field | Post-Yaas reporting links rainwater breaching embankments with continuing saline inundation of farmland [2] | A plausible observed cascade requiring local breach and salinity observations | Exact causal contribution of surge versus river water versus rain at each farm |
| Multiple rivers + high tide | Mahanadi, Brahmani, and Baitarani floodwaters intermingle in a common delta; high tide aggravates the problem [5] | A documented spatially and multivariately compounding Odisha mechanism | Station-to-station conditional probabilities without gauge analysis |
| Cyclone/rain + crop disease | Fani assessment reports fungal attack on mung following heavy-rain inundation [30] | One documented crop-specific compound impact | A universal flood -> blast or flood -> BPH rule |
| Flood/cyclone + market disruption | Fani evidence describes perishability, distress selling, middlemen dependence, connectivity and cold-chain gaps [30] | A documented hazard -> access -> price mechanism | A farm-gate price elasticity or mandi closure probability |
| Flood + livelihood vulnerability | Bhadrak evidence shows recovery differed by wealth, tenure, migration, asset sale, and access to assistance [37] | Impact is compounded by social and financial preconditions | A universal debt transition coefficient |
| Drought -> flood swing | Compound-event literature permits preconditioned and successive hazards [12] | Drought can be represented as a precondition affecting soil, assets, debt, and water storage | That drought causes the next flood, or that an Odisha Hawkes excitation parameter exists |

### Copula implementation and the missing dependence value

For a Gumbel copula,

`C(u,v) = exp(-(((-ln u)^theta + (-ln v)^theta)^(1/theta)))`, with `theta >= 1` and Kendall dependence `tau = 1 - 1/theta`.

The Alappuzha study establishes that Gumbel-Hougaard, Clayton, and Frank families are reasonable candidates for rainfall-water-level dependence [33]. The Peninsular India study establishes the relevance of precipitation, runoff, and soil moisture to Mahanadi compound flooding [9]. However, the accessible evidence does not provide a validated Gumbel `theta` for Odisha surge-rain, surge-river, or rain-river pairs. The prototype should fit and compare candidate families using Odisha event pairs, report confidence intervals and tail diagnostics, and fall back to empirical resampling when fit is unstable.

**Decision-ready insight:** The Odisha triple is real as a mechanism, but its dependence values remain a calibration task. Reporting a borrowed Gumbel number as an Odisha fact would be false precision.

## 5. COVERAGE TABLE

| Required element | Evidence coverage | Quantification status | Prototype status |
|---|---|---|---|
| Cyclone -> surge -> salinity -> soil -> next season | Fani/Yaas surge and Yaas saline fields documented [29][28][2] | Surge strong; local salinity dose-response and persistence missing | **Build now with transfer prior** |
| Cyclone -> rain -> river -> embankment -> field | Rain, shared delta, high tide, and observed embankment pathway documented [5][28][2] | Local edge probabilities and lags missing | **Build as observable states** |
| Flood -> waterlogging -> root rot -> blast -> market | Waterlogging loss, Fani fungal damage, blast biology, and market disruption documented [18][30][25] | No validated root-rot or flood-to-blast transition | **Partial; prohibit deterministic disease claim** |
| Flood -> seed loss -> seed gap -> sowing -> credit -> debt | Seed-chain, credit-access, lender, and recovery mechanisms documented [30][37] | No seed-loss, delay-yield, interest, or debt coefficients | **State machine yes; predictive scoring later** |
| Drought -> flood | Supported as a compound-event class, not as direct causation [10] | Odisha dependence absent | **Scenario only** |
| Flood -> recharge -> water security | Managed UTFI intervention quantified [36] | Odisha hydrogeology and water quality absent | **Optional positive node** |
| Flood -> silt -> soil fertility | Sediment and soil-health association documented outside Odisha [17] | Yield benefit absent | **Monitor only** |
| Fish ingress -> paddy yield | Managed paddy-fish output documented [38] | No evidence for accidental ingress or rice-yield gain | **Do not claim** |
| Bayesian causal inference | Two strong flood precedents [20][13] | Requires Odisha CPTs | **Core prototype** |
| Cascade failure analogy | Critical-loading mechanism documented [26] | No direct coefficient transfer | **Use architecture, not parameters** |
| Hawkes self-excitation | Method and seismology use documented [11] | Cyclone-to-flood excitation unproved | **Research toggle, off by default** |
| System dynamics | Rice-household CLD precedent documented [16] | Lacks calibrated stocks and flows | **Explanatory dashboard only** |
| Monte Carlo + convergence | Repeated sampling and sequential gates supported [27] | Gate tolerances are product requirements | **Core prototype** |
| 95% CVaR decisions | Convex sample optimization supported [15] | Action costs and preferences require elicitation | **Core prototype** |
| Evolving incident state | IMD and CAP supply stages and update semantics [22][24] | Farm transitions must be designed | **Core prototype** |
| SMS/IVR for low literacy | Required by the problem statement | Usability effectiveness unmeasured | **Demonstrate with Odia scripted calls** |

The buildable core has high coverage. The weakest claims are the proposed pest/disease transmissions, accidental fish benefit, drought-caused flood, and local economic coefficients.

## 6. WHAT IS MISSING

1. **Odisha joint-hazard calibration.** No verified Gumbel `theta`, Kendall `tau`, or conditional return period was found for cyclone surge + rain + river flow in Odisha. Mahanadi-scale multivariate work demonstrates the need, not the coastal coefficient [9].

2. **Farm-scale inundation functions.** IMD supplies district-scale wind, rain, and surge, but the engine still needs DEM, embankment condition, drainage capacity, tide, canal operation, and field elevation to predict depth and duration. Static BNs are known to miss delayed peaks and levee failures [13].

3. **Odisha salinity response and persistence.** The **1.9 dS/m** threshold comes from California varieties and conditions [23]. Required local data include EC in field water and soil, variety, crop stage, texture, rainfall leaching, drainage, and next-season recovery.

4. **Root-rot, blast, and BPH transition probabilities.** Existing sources establish severe potential losses but not the requested flood-caused transitions [19][25]. A useful model requires scouting labels, leaf wetness, humidity, temperature, inoculum or migration pressure, planting date, and control history.

5. **Seed and market coefficients.** Fani documents urgent seed-chain repair, distress selling, and credit barriers [30], but not seed stocks lost per inundation depth, sowing-delay yield penalties, mandi price elasticity, or road-closure duration.

6. **Debt dynamics by tenure and gender.** Bhadrak evidence shows unequal assistance and recovery, especially for landless households [37]. The graph needs loan balance, lender, interest, repayment schedule, compensation eligibility, tenancy, SHG/MFI exposure, and asset sales.

7. **Positive-cascade validation.** Managed recharge, managed rice-fish, and flood-sediment systems cannot be relabeled as automatic benefits of uncontrolled flooding [38][36]. Odisha pilots must test hydrogeology, contamination, salinity, infrastructure, rice yield, fish survival, and economics.

8. **Intervention cost and feasibility data.** CVaR cannot choose sensibly among early harvest, drainage, seed movement, livestock evacuation, delayed sowing, or crop switching without costs, labor, lead time, equipment, storage, and farmer preferences.

9. **Communication validation.** The state machine can emit Odia SMS/IVR, but comprehension, trust, callback behavior, shared-phone access, dialect, and message fatigue require farmer testing.

**Decision-ready insight:** These gaps do not block a prototype. They determine which outputs must be probability ranges or `unknown`, rather than authoritative-looking point estimates.

## 7. HOW IT FEEDS THE ENGINE

### 7.1 Data and causal layers

The engine should maintain three linked objects:

1. **Incident**: IMD bulletin ID, CAP identifier, issued time, onset, expiry, track ensemble, wind, rain, surge, tide, and update/cancel references. CAP explicitly supports initial Alert, Update, Cancel, Ack, and Error messages [24].
2. **Farm state**: geolocation, elevation, embankment/drainage relation, crop, variety, stage, seed inventory, livestock, assets, soil-water EC, observed depth/duration, market route, household vulnerability, and last confirmed action.
3. **Cascade graph**: time-sliced nodes and typed edges, each with an evidence grade and parameter provenance.

A Bayesian network factorizes the current slice as:

`P(X_1,...,X_n | evidence) = product_i P(X_i | Parents(X_i))`.

A time-sliced model then adds `X_i(t-1) -> X_i(t)` persistence and selected lagged cross-node edges. This fixes the principal limitation identified for static flood BNs [13].

### 7.2 Monte Carlo propagation

For simulation draw `s`:

1. Draw one coherent hazard vector from IMD ensembles and fitted dependence structure.
2. Propagate rain, river, tide, surge, breach, field depth, duration, and salinity in topological and time order.
3. Draw crop response conditional on crop, stage, variety, duration, and salinity.
4. Propagate seed, market, credit, and recovery states only through supported conditional tables or explicitly labeled scenario priors.
5. Record node losses, action feasibility, warning lead time, and positive outcomes such as managed recharge.

Monte Carlo is repeated random sampling [27]. It should stop through a convergence gate, not a presentation-friendly round number. Use an independent pilot stage to estimate variance, then a main stage. Require the configured absolute or relative confidence-interval precision for critical node probabilities, expected loss, and CVaR; prevent premature termination and report when the maximum computation budget is reached without convergence [27].

### 7.3 CVaR at each node

For loss samples `L_s(a)` under action `a`, estimate 95% CVaR as:

`CVaR_0.95(a) = min_eta [eta + (1/(0.05*N)) * sum_s max(L_s(a)-eta, 0)]`.

This sample objective is convex and piecewise linear [15]. At every loss-bearing node, calculate expected loss, 95th percentile, and 95% CVaR. At decision-enabled nodes, select an action using:

`a* = argmin_a {CVaR_0.95(total loss | a) + action cost(a) + infeasibility penalty(a)}`.

Examples include harvest now versus wait, move seed versus protect in place, open drainage versus retain water, or sow now versus wait for an EC test. CVaR should not create an action where none exists; at a pure sensor node it is a risk diagnostic.

### 7.4 Advisory state machine

| State | Entry evidence | Graph operation | SMS/IVR behavior |
|---|---|---|---|
| `MONITOR` | Seasonal baseline | Update climatology and farm inventory | No alert; periodic preparedness prompt |
| `PRE_CYCLONE_WATCH` | IMD 72-hour watch [22] | Initialize event graph and broad ensemble | Short heads-up; ask farmer to confirm crop and assets |
| `CYCLONE_ALERT` | IMD at least 48 hours [22] | Evaluate feasible preventive actions | Prioritized checklist with confirmation keys |
| `CYCLONE_WARNING` | IMD at least 24 hours; landfall point available [22] | Recompute action CVaR with narrowed forecast | One highest-value action per call, then repeat/acknowledge |
| `POST_LANDFALL_OUTLOOK` | IMD at least 12 hours before expected landfall [22] | Predict inland rain, river, and access cascade | Update rather than duplicate the incident |
| `IMPACT_SUSPECTED` | Remote sensing, gauges, forecast threshold | Raise observation requests; widen uncertainty | Ask depth, salinity signs, crop condition, access status |
| `IMPACT_CONFIRMED` | Farmer, sensor, or official observation | Condition BN on observations | Farm-specific safety and loss-limiting advice |
| `RESPONSE` | Hazard ongoing or access impaired | Disable unsafe actions; route rescue and essential needs | IVR first for urgent safety; concise SMS record |
| `RECOVERY` | Water recession and access restored | Activate seed, soil, market, credit, and livelihood nodes | Sequenced tasks, not a single recovery list |
| `NEXT_SEASON` | Soil/seed/water decision window | Carry salinity, debt, recharge, seed, and variety state forward | Crop/variety recommendation with uncertainty and test needs |
| `CLOSED` | Recovery criteria met or CAP Cancel | Freeze event audit trail; retain learned parameters | Final status and feedback request |

The broader disaster cycle includes prevention, mitigation, preparedness, response, and recovery [7]. FAO also emphasizes linking immediate agricultural relief to restoration of production systems and longer-term resilience [8]. Thus `RECOVERY` must feed `NEXT_SEASON`; it is not an end state.

### 7.5 Buildable demonstration

- **Replay Fani** using the official track, wind, rain, and surge, then show the posterior distribution for crop area/loss against the documented **108,220 ha** and **INR 1,304.58 crore** anchors [30].
- **Replay Yaas** and expose the surge + tide + rain + embankment + salinity chain, including an uncertainty band rather than a made-up salinity value.
- **CVaR harvest decision**: compare wait, partial early harvest, and immediate harvest using forecast loss, harvestable maturity, labor, price, and action cost.
- **Swarna-Sub1 decision**: show next-season variety advice changing with the posterior distribution of submergence duration, using the Odisha trial response [14].
- **Positive-cascade switch**: show recharge benefit only when the farm is linked to a validated managed-recharge structure; otherwise output `not applicable`.
- **Odia SMS/IVR trace**: present the same incident as watch, alert, impact update, recovery, and next-season advice with CAP-linked updates and acknowledgements.

## 8. REAL-vs-FILLER + NOISE LOG

| Claim or module | Classification | Why | Product rule |
|---|---|---|---|
| Fani/Yaas replay with IMD observations | **REAL** | Official wind, rain, surge, forecast-error, and loss anchors exist [29][28] | Demonstrate |
| Shared-delta compound flood graph | **REAL** | Odisha evidence explicitly describes intermingling rivers and high-tide aggravation [5] | Demonstrate |
| Dynamic BN for farm impacts | **REAL, transferable** | Strong probabilistic flood-loss and cascade precedents exist [20][13] | Build and label local versus borrowed CPTs |
| Swarna-Sub1 duration response | **REAL, local** | Randomized Odisha evidence with quantified response [14] | Use as local decision edge |
| 32.9% waterlogging loss as Odisha truth | **NOISE if localized** | It is a global pooled result with strong heterogeneity [18] | Use only as wide prior |
| California 1.9 dS/m threshold as Odisha truth | **NOISE if copied** | Different varieties, soil, climate, and management [23] | Use functional form, recalibrate |
| Published Odisha Gumbel dependence value | **MISSING** | Candidate copulas and Mahanadi relevance exist, but no verified Odisha parameter was recovered [33][9] | Fit locally; do not quote one |
| Hawkes proof that a cyclone causes the next flood | **FILLER** | Hawkes describes self-exciting arrival clustering; retrieved applications emphasize seismology [11] | Keep off by default; never state causality from excitation alone |
| SIR BPH outbreak after flood | **FILLER today** | Severe BPH losses are real, but flood is not established as the transmission trigger [19][6] | Require surveillance and migration data |
| Flood directly causes blast | **FILLER** | Blast biology and loss exist, but the requested flood transition is unverified [25] | Model weather/inoculum pathway only |
| Flood automatically recharges aquifers | **FILLER without infrastructure** | Quantified benefit comes from a designed pond, filters, and recharge wells [36] | Positive edge only for suitable managed sites |
| Fish ingress improves paddy yield | **FILLER** | Evidence concerns managed stocking, channels, and water control [38] | Replace with managed rice-fish option |
| Silt always improves soil and yield | **FILLER** | Soil-health association exists, but crop-yield and economic data were absent [17] | Test salinity and contamination first |
| CVaR at every node | **REAL with qualification** | CVaR is mathematically tractable [15] | Calculate at loss nodes; optimize only at action nodes |
| One-shot advisory message | **ANTI-PATTERN** | IMD phases and CAP updates support an evolving incident [22][24] | Maintain one versioned state machine |

**Noise policy:** Every UI number should carry one of four badges: `ODISHA-MEASURED`, `TRANSFER-PRIOR`, `SCENARIO-ASSUMPTION`, or `UNKNOWN`. An advanced equation without a validated input remains an assumption, not intelligence.

## 9. VERDICT

**GO, with a deliberately narrow mathematical core.** The concept is technically credible and differentiated if the prototype demonstrates:

1. a typed, signed, time-sliced cascade graph;
2. event replay for Fani and Yaas;
3. a dynamic BN updated by hyperlocal observations;
4. joint hazard sampling without fabricated dependence values;
5. Monte Carlo propagation with visible convergence status;
6. 95% CVaR action selection;
7. one rigorously qualified positive cascade; and
8. an IMD/CAP-linked Odia SMS/IVR state machine.

The strongest pitch is not "no existing advisory has sophisticated math." That exclusivity claim was not established. The defensible pitch is: **this prototype makes causal assumptions, uncertainty, tail risk, and cross-season consequences explicit in one auditable advisory incident.**

A credible judging demonstration should show two contrasts. First, under the same cyclone warning, a high-field farm with mature paddy receives different advice from a low-field farm behind a weak embankment with newly transplanted rice. Second, when a farmer reports saline water or observed flood depth, the posterior and recommendation change immediately rather than waiting for a new generic bulletin.

The hard stop is scientific overclaiming. Do not publish an Odisha copula coefficient that was never estimated; do not convert correlation into causation; do not equate managed recharge with ordinary flooding; and do not claim that flood automatically causes BPH or blast. These constraints strengthen, rather than weaken, the engine's credibility.

## Synthesis

| Dimension | Static threshold advisory | Full "everything model" | Recommended cascade engine |
|---|---|---|---|
| Mechanism | One hazard crosses one threshold | Many methods run without clear roles | Typed dynamic DAG; copula only for joint inputs; BN for inference; MC for propagation; CVaR for action |
| Scope | Warning and immediate action | Hazard, crop, disease, market, debt, recovery all predicted at once | End-to-end states, but only evidence-backed edges are quantified |
| Time horizon | Hours to landfall | Potentially unlimited | 72-hour watch through next season |
| Evidence base | Operational forecasts | Often borrowed parameters | Fani/Yaas anchors, Odisha crop trial, transferable priors with explicit provenance |
| Tail risk | Usually absent | Complex but opaque | 95% CVaR at loss and decision nodes |
| Positive effects | Ignored | May be overstated | Managed recharge, sediment, and rice-fish represented conditionally |
| Main trade-off | Simple but myopic | Impressive but unidentifiable | More engineering work, but auditable and calibratable |
| Failure mode | Misses cascading losses | False precision and model theater | Explicit unknowns and conservative fallback advisories |

The non-obvious tension is that mathematical sophistication and scientific credibility can move in opposite directions. Copulas, Hawkes processes, SIR models, and system dynamics add value only when each has a distinct data-generating role. Otherwise they create more parameters than the Odisha evidence can identify.

The second tension is between harmful and beneficial water. The same monsoon flow can create salinity, waterlogging, disease pressure, asset loss, aquifer recharge, sediment delivery, or fish production depending on tide, water quality, infrastructure, timing, crop stage, and management. That is precisely why a signed conditional graph is superior to a universal "flood bad" score [17][36].

Finally, the power-grid analogy contributes one durable idea: near capacity limits, one failure increases stress elsewhere and can sharply enlarge the cascade [26]. In Odisha agriculture, the analogues are saturated drainage, breached embankments, depleted seed stocks, blocked market access, and exhausted household credit. The coefficients cannot be transferred from power systems, but the search for critical nodes can: protect the node whose failure most increases downstream CVaR.

## References

1. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Cyclone Fani 2019 DLNA Report*. https://www.osdma.org/publication/cyclone-fani-2019-dlna-report
2. *Cyclone Yaas aftermath: Odisha farmers in a fix over sowing Kharif crop*. https://www.downtoearth.org.in/agriculture/cyclone-yaas-aftermath-odisha-farmers-in-a-fix-over-sowing-kharif-crop-77568
3. *Sendai Framework for Disaster Risk Reduction 2015-2030 | UNDRR*. https://www.undrr.org/publication/sendai-framework-disaster-risk-reduction-2015-2030
4. *Cyclone Fani Damage, Loss, and Needs Assessment | IRP*. https://recovery.preventionweb.net/publication/documents-and-publications/cyclone-fani-damage-loss-and-needs-assessment
5. *ODISHA STATE DISASTER MANAGEMENT AUTHORITY | Flood*. https://www.osdma.org/preparedness/one-stop-risk-management-system/flood/
6. *BPH, Nilaparvata lugens Stal,Rice brown planthopper (BPH),Rice pests of DSS, croppest DSS *. http://www.icar-crida.res.in:8080/naip/bph.jsp
7. *The Disaster Management Cycle: 5 Key Stages UCF Online*. https://www.ucf.edu/online/leadership-management/news/the-disaster-management-cycle
8. *fao.org*. https://www.fao.org/4/X6874E/x6874e01.htm
9. *Assessing compound flood drivers in Peninsular India: Multivariate copula-based approach - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0301479725038514
10. *A typology of compound weather and climate events | Nature Reviews Earth & Environment*. https://www.nature.com/articles/s43017-020-0060-z
11. *Hawkes Models And Their Applications*. https://arxiv.org/html/2405.10527v1
12. *Chapter 11: Weather and Climate Extreme Events in a Changing Climate | Climate Change 2021: The Physical Science Basis*. https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-11/
13. *Bayesian network modeling of flood cascade and climate risks in the Pearl River Delta | npj Natural Hazards*. https://www.nature.com/articles/s44304-025-00115-1
14. [
            Flood-tolerant rice reduces yield variability and raises expected yield, differentially benefitting socially disadvantaged groups - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC3837307)
15. *-*. https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf
16. *Open Access proceedings Journal of Physics: Conference series*. https://iopscience.iop.org/article/10.1088/1755-1315/1323/1/012009/pdf
17. *Enhancing Soil Health Through Sediment Deposition in Flood‐Based Agricultural Systems: Evidence From the Mekong Delta, Vietnam - Ho - 2026 - Applied and Environmental Soil Science - Wiley Online Library*. https://onlinelibrary.wiley.com/doi/full/10.1155/aess/9529778
18. *Frontiers | How Does the Waterlogging Regime Affect Crop Yield? A Global Meta-Analysis*. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.634898/full
19. *BROWN PLANTHOPPER RESISTANT RICE: A JOURNEY FROM LANDRACES TO VARIETIES*. https://icar-crri.in/wp-content/uploads/2024/08/NRRI_Research-Bulletin-No-53.pdf
20. *NHESS - BN-FLEMOΔ: a Bayesian-network-based flood loss estimation model for adaptation planning in Ho Chi Minh City, Vietnam*. https://nhess.copernicus.org/articles/25/2845/2025
21. [
            Salinity Stress in Rice: Multilayered Approaches for Sustainable Tolerance - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC12250271/)
22. *Four Stage Warning*. https://rsmcnewdelhi.imd.gov.in/four-stage-warning.php
23. *Pdf Pubs*. https://www.ars.usda.gov/arsuserfiles/20361500/pdf_pubs/P1837.pdf
24. *Common Alerting Protocol*. https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html
25. [
            The Devastating Rice Blast Airborne Pathogen Magnaporthe oryzae—A Review on Genes Studied with Mutant Analysis - PMC
        ](https://pmc.ncbi.nlm.nih.gov/articles/PMC10055536)
26. *Criticality in a cascading failure blackout model - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S0142061506000810
27. *arxiv.org*. https://arxiv.org/pdf/2510.22688
28. *26 77Afd4 Preliminary Report Yaas During 23 27 May 2021*. https://rsmcnewdelhi.imd.gov.in/uploads/report/26/26_77afd4_Preliminary%20Report%20YAAS%20during%2023-27%20May%202021.pdf
29. *rsmcnewdelhi.imd.gov.in*. https://rsmcnewdelhi.imd.gov.in/uploads/archive/60/60_a53fa0_fani.pdf
30. *untitled*. https://www.osdma.org/wp-content/uploads/2019/08/Cyclone-Fani-2019-Odisha-DLNA-Report.pdf
31. *Future climate risk from compound events | Nature Climate Change*. https://www.nature.com/articles/s41558-018-0156-3
32. *3 - Changes in Climate Extremes and their Impacts on the Natural Physical Environment*. https://www.ipcc.ch/site/assets/uploads/2018/03/SREX-Chap3_FINAL-1.pdf
33. *Flood risk analysis and mapping under compound hazards: A copula approach for tropical coastal district of Alappuzha, India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S1570644322000715
34. *Project : Underground Taming of Floods for Irrigation (UTFI) - Project : Underground Taming of Floods for Irrigation (UTFI)*. https://utfi.iwmi.org/
35. *Ecosystem services analysis for sustainable agriculture expansion: Rice-fish co-culture system breaking through the Hu Line - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S1470160X21010505
36. *Water Policy Brief*. https://cgspace.cgiar.org/bitstreams/05c06c00-b389-43aa-8a1c-dc3d7d580795/download
37. *Flood shocks and post-disaster recovery of households: An empirical analysis from rural Odisha, India - ScienceDirect*. https://www.sciencedirect.com/science/article/pii/S2212420923005502
38. *Paddy-cum-fish-culture*. https://meen.arunachal.gov.in/uploads/publications/paddy-cum-fishculture.pdf
