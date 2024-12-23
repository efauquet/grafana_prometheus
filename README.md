# Docker

- `docker-compose build`
- `docker-compose up`

# Check Prometheus Target Health

- Go to: http://localhost:9090/
- Go to Status > Target Health (or http://localhost:9090/targets)
![img.png](img/img.png)

# Add Prometheus as a Data Source

- Go to: http://localhost:3000
- Log in with user: admin pwd: admin 
- Change password
- Go to: Home > Connections > Data Sources.
- Add a new data source:
    - Type: Prometheus
    - URL: http://prometheus:9090
    - Leave the rest as default
    - Save & Test.


# Create a Dashboard

TODO copy requests here

# Generate API calls

- run _request_script/main.py_