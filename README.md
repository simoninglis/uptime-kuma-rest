# Uptime Kuma API Wrapper

This Flask application serves as a RESTful API wrapper for Uptime Kuma, providing a simplified interface for interacting with Uptime Kuma's monitoring functionalities. It allows for easy integration and management of monitors within Uptime Kuma through a set of HTTP endpoints.

## Features

- List Monitors: Retrieve a list of all configured monitors.
- Monitor Details: Fetch detailed information about a specific monitor.
- Pause/Resume Monitor: Control the operational state of a monitor by pausing or resuming it.
- Monitor Status: Check the current status of a monitor (active/inactive).
- Service Status: Get the operational status of the service being monitored (UP, DOWN, PENDING).

## Getting Started

### Prerequisites

- Docker (if using Docker for deployment)
- Python 3.8 or newer (if running locally without Docker)
- An Uptime Kuma instance
- Flask
- Flasgger for Swagger UI documentation

### Installation

#### Using Docker

1. Clone the repository to your local machine:
```bash
   git clone https://example.com/uptime-kuma-api-wrapper.git
   cd uptime-kuma-api-wrapper
```

2. Build the Docker image:
```bash
   docker build -t uptime-kuma-api-wrapper .
```

3. Run the Docker container, replacing the environment variables with your actual Uptime Kuma API credentials and base URL:

```bash
   docker run -d -p 5000:5000 --env UPTIME_KUMA_USERNAME=your_username --env UPTIME_KUMA_PASSWORD=your_password --env UPTIME_KUMA_BASE_URL=your_uptime_kuma_instance_url uptime-kuma-api-wrapper
```

#### Running Locally

1. Follow the first step above to clone the repository.

2. Install the required Python packages:
```bash
   pip install -r requirements.txt
```

3. Set up environment variables by creating a .env file in the project root with the following contents, replacing the values with your actual Uptime Kuma API credentials and base URL:

```bash
UPTIME_KUMA_USERNAME=your_username
UPTIME_KUMA_PASSWORD=your_password
UPTIME_KUMA_BASE_URL=http://your-uptime-kuma-instance.com
```

4. Start the Flask application:
```bash
   python app.py
```

The application will start on http://localhost:5000/. Swagger UI documentation can be accessed at http://localhost:5000/apidocs.

## Usage

### Using curl to Interact with the API

#### Pause a Monitor

To pause a monitor, replace monitor_id with the actual ID of the monitor you wish to pause:

```bash
curl -X POST http://localhost:5000/monitor/pause/<monitor_id>
```

#### Resume a Monitor

To resume a monitor, replace monitor_id with the actual ID of the monitor you wish to resume:

```bash
curl -X POST http://localhost:5000/monitor/resume/monitor_id
```

#### Get Monitor's Active Status

To check if a monitor is active, replace monitor_id with the actual ID of the monitor:

```bash
curl http://localhost:5000/monitor/active/monitor_id
```

## Contributing

Contributions to this project are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear, descriptive messages.
4. Push your branch and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
