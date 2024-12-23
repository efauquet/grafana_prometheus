import requests
import time
import random

app_url = "http://localhost:8080/"

# in seconds
duration = 180
interval = 2.5


def generate_random_data():
    data = {
        "metric_1": random.randint(1, 100),
        "metric_2": random.random() * 100,
        "status": "ok"
    }
    return data


def send_data():
    data = generate_random_data()  # Generate random data
    try:
        response = requests.post(app_url, json=data)
        if response.status_code == 200:
            print(f"Data sent successfully: {data}")
        else:
            print(f"Failed to send data, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")


def get_data():
    try:
        response = requests.get(app_url)
        if response.status_code == 200:
            print("data received")
        else:
            print("get failed")
    except requests.exceptions.RequestException as e:
        print(f"request error: {e}")


if __name__ == "__main__":
    start_time = time.time()
    while time.time() - start_time < duration:
        get_data()
        # send_data()
        time.sleep(interval)
    print(f"Data generation completed for {duration}s with a {interval}s interval.")
