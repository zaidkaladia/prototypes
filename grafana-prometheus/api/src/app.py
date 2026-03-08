from flask import Flask, Response
import requests
import time
import threading
from prometheus_client import Counter, Histogram, Gauge, generate_latest

app = Flask(__name__)

# -----------------------------
# Prometheus Metrics
# -----------------------------

# Current Bitcoin price
BITCOIN_PRICE = Gauge(
    "bitcoin_price_usd",
    "Current Bitcoin price in USD"
)

# Successful scrapes
SCRAPE_SUCCESS = Counter(
    "scrape_success_total",
    "Total successful scrapes"
)

# Rate limit errors (HTTP 429)
RATE_LIMIT = Counter(
    "scrape_rate_limit_total",
    "Total API rate limit responses"
)

# Scrape duration
SCRAPE_DURATION = Histogram(
    "scrape_duration_seconds",
    "Time taken to scrape Bitcoin price"
)

# -----------------------------
# Scraper Function
# -----------------------------

def scrape_bitcoin():

    start_time = time.time()

    try:

        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
            timeout=5
        )

        if response.status_code == 429:
            print("Rate limit hit")
            RATE_LIMIT.inc()
            return

        response.raise_for_status()

        data = response.json()

        price = data["bitcoin"]["usd"]

        BITCOIN_PRICE.set(price)

        SCRAPE_SUCCESS.inc()

        print(f"Bitcoin price updated: ${price}")

    except Exception as e:

        print("Scrape error:", e)

    duration = time.time() - start_time
    SCRAPE_DURATION.observe(duration)

# -----------------------------
# Background Scraper Loop
# -----------------------------

def scraper_loop():

    while True:

        scrape_bitcoin()

        # Wait 20 seconds to avoid rate limits
        time.sleep(20)

# -----------------------------
# Flask Routes
# -----------------------------

@app.route("/")
def home():
    return "Bitcoin scraper is running"


@app.route("/metrics")
def metrics():

    return Response(
        generate_latest(),
        mimetype="text/plain"
    )

# -----------------------------
# Start Application
# -----------------------------

if __name__ == "__main__":

    # Start background scraper
    thread = threading.Thread(
        target=scraper_loop,
        daemon=True
    )

    thread.start()

    app.run(
        host="0.0.0.0",
        port=4000,
        use_reloader=False
    )