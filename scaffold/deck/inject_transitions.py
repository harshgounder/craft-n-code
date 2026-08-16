import zipfile, shutil, re, sys

SRC = sys.argv[1] if len(sys.argv) > 1 else "KrishiSetu-Round0-20260816.pptx"
TMP = SRC + ".tmp"
TRANS = '<p:transition spd="med"><p:fade/></p:transition>'

zin = zipfile.ZipFile(SRC, "r")
zout = zipfile.ZipFile(TMP, "w", zipfile.ZIP_DEFLATED)
count = 0
for item in zin.infolist():
    data = zin.read(item.filename)
    if re.match(r"ppt/slides/slide\d+\.xml$", item.filename):
        xml = data.decode("utf-8")
        if "clrMapOvr" in xml and "<p:transition" not in xml:
            xml = xml.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + TRANS, 1)
            data = xml.encode("utf-8")
            count += 1
    zout.writestr(item, data)
zin.close()
zout.close()
shutil.move(TMP, SRC)
print(f"injected fade transition into {count} slides")
