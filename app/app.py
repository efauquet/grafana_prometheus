from flask import Flask
from prometheus_client import Counter, generate_latest, Histogram

app = Flask(__name__)
request_counter = Counter("requests_total", "Total Requests", ["method", "endpoint"])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency', ['method', 'endpoint'])


@app.route("/")
def index():
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        request_counter.labels(method="GET", endpoint="/").inc()
        return "Hello, World!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
