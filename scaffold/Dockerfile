# Craft N Code 2026 shared scaffold - one-command container image
FROM python:3.11-slim

WORKDIR /app

# curl is required for the HEALTHCHECK probe against /health
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

# runtime only needs the python pieces; prune demo/build junk from the image
RUN rm -rf deck/node_modules backups dist

EXPOSE 8137

HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -fsS http://127.0.0.1:8137/health || exit 1

CMD ["python3", "webapp/serve.py", "--host", "0.0.0.0", "--port", "8137"]
