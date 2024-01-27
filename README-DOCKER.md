# Uptime Kuma API Wrapper Docker Image

This Docker image contains the Uptime Kuma API Wrapper, a Flask application that serves as a RESTful API wrapper for Uptime Kuma. It provides a simplified interface for interacting with Uptime Kuma's monitoring functionalities, allowing easy integration and management of monitors through HTTP endpoints.

## Features

- List Monitors: Retrieve all configured monitors.
- Monitor Details: Get detailed information about specific monitors.
- Pause/Resume Monitor: Control the operational state of monitors.
- Monitor Status: Check whether a monitor is active or inactive.
- Service Status: Determine the operational status of monitored services (UP, DOWN, PENDING).

## Quick Start

### Running with Docker

You can quickly start the Uptime Kuma API Wrapper using Docker without needing to clone the repository or build the image locally.

Pull the image from Docker Hub:

```bash
docker pull gronax/uptime-kuma-rest:latest
```

Run the Docker container, replacing the environment variables with your Uptime Kuma API credentials and the base URL of your Uptime Kuma instance:

```bash
docker run -d -p 5000:5000 \
  --env UPTIME_KUMA_USERNAME=your_username \
  --env UPTIME_KUMA_PASSWORD=your_password \
  --env UPTIME_KUMA_BASE_URL=your_uptime_kuma_instance_url \
  gronax/uptime-kuma-rest:latest
```
### Using Docker Compose
Alternatively, you can use Docker Compose to run the Uptime Kuma API Wrapper. Create a docker-compose.yml file with the following content:

```yaml
version: '3'
services:
  uptime-kuma-api-wrapper:
    image: gronax/uptime-kuma-rest:latest
    ports:
      - "5000:5000"
    environment:
      UPTIME_KUMA_USERNAME: your_username
      UPTIME_KUMA_PASSWORD: your_password
      UPTIME_KUMA_BASE_URL: your_uptime_kuma_instance_url
```

Run the service using:

```bash
docker-compose up -d
```

## Interacting with the API
Once the container is running, you can interact with the API as follows:

Pause a Monitor: curl -X POST http://localhost:5000/monitor/pause/<monitor_id>
Resume a Monitor: curl -X POST http://localhost:5000/monitor/resume/monitor_id
Get Monitor's Active Status: curl http://localhost:5000/monitor/active/monitor_id
Swagger UI documentation can be accessed at http://localhost:5000/apidocs.

## Contributing
We welcome contributions! If you would like to contribute to the project, please follow the standard GitHub fork and pull request workflow.

## License
This project is released under the MIT License. See the LICENSE file in the GitHub repository for more details.