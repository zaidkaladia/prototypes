# Scraper Monitoring System (Prometheus + Grafana)

A production-style monitoring setup for a scraping service built using Flask, Prometheus, and Grafana.  
The service scrapes real-time Bitcoin price data and exposes metrics that are collected by Prometheus and visualized using Grafana dashboards.

This project demonstrates how scraping systems can be monitored in real time using modern observability tools.

---

## Architecture

Flask Scraper → Prometheus → Grafana

The scraping service exposes metrics through a `/metrics` endpoint which are periodically scraped by Prometheus. Grafana then queries Prometheus to visualize these metrics in dashboards.

---

## Tech Stack

- Python (Flask)
- Prometheus
- Grafana
- Docker
- Docker Compose

---

## Features

- Real-time scraping of Bitcoin price
- Prometheus metrics instrumentation
- Grafana monitoring dashboards
- Scrape success and failure tracking
- Scrape latency monitoring
- Simulated scraper failures
- Dockerized deployment

---

## Metrics Exposed

The Flask service exposes the following Prometheus metrics:

### Scraping Metrics

| Metric | Description |
|------|------|
| scrape_success_total | Total successful scrapes |
| scrape_failure_total | Total failed scrapes |
| scrape_duration_seconds | Histogram of scraping latency |

### Data Metrics

| Metric | Description |
|------|------|
| bitcoin_price_usd | Current Bitcoin price in USD |

### System Metrics (Auto Exposed)

Prometheus Python client automatically exposes system metrics such as:

- CPU usage
- Memory usage
- Python garbage collection stats

---

## Dashboard Metrics

Grafana dashboards visualize the following:

- Live Bitcoin price
- Scrapes per second
- Scraper failure count
- Scrape latency (P95)

---

## Running the Project

Clone the repository:

git clone https://github.com/yourusername/scraper-monitoring

cd scraper-monitoring

Start the monitoring stack:
docker-compose up --build


---

## Access the Services

Grafana Dashboard: http://localhost:3000


Prometheus Server: http://localhost:9090


Flask Scraper API: http://localhost:4000


Metrics Endpoint: http://localhost:4000/metrics


---

## How the Scraper Works

A background thread runs every 10 seconds and performs the following:

1. Fetches the current Bitcoin price
2. Updates Prometheus metrics
3. Tracks success or failure
4. Records scrape latency

Prometheus collects these metrics and Grafana visualizes them.

---

## Failure Simulation

To demonstrate monitoring capabilities, the scraper randomly simulates failures.

This allows Grafana dashboards to show failure spikes and test alerting conditions.

---

## Deployment

The entire stack is containerized using Docker Compose and can be deployed on any cloud server.

Example deployment environments:

- AWS EC2
- DigitalOcean Droplet
- Local development machine

---

## Example Use Cases

This monitoring setup is useful for:

- Web scraping pipelines
- Data collection services
- API monitoring
- Background job monitoring
- Observability demonstrations

---

## Screenshots

(Add Grafana dashboard screenshots here)

---

## Future Improvements

- Grafana alerting for scraper failures
- Auto provisioning of dashboards
- Support for multiple scraping targets
- Slack/Email alerts

---

## Author

Zaid Kaladia