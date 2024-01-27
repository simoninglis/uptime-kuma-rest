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

- Python 3.8 or newer
- An Uptime Kuma instance
- Flask
- Flasgger for Swagger UI documentation

### Installation

1. Clone the repository to your local machine:
   git clone https://example.com/uptime-kuma-api-wrapper.git
   cd uptime-kuma-api-wrapper

2. Install the required Python packages:
   pip install -r requirements.txt

3. Set up environment variables by creating a .env file in the project root with the following contents:
   UPTIME_KUMA_USERNAME=your_username
   UPTIME_KUMA_PASSWORD=your_password
   UPTIME_KUMA_BASE_URL=http://your-uptime-kuma-instance.com

### Running the Application

Start the Flask application by running:
python app.py
The application will start on http://localhost:5000/. Swagger UI documentation can be accessed at http://localhost:5000/apidocs.

## Usage

Here are some example requests you can make to the API:

- List Monitors: GET /monitors
- Get Monitor Details: GET /monitor/{monitor_id}
- Pause a Monitor: POST /monitor/pause/{monitor_id}
- Resume a Monitor: POST /monitor/resume/{monitor_id}
- Check if Monitor is Active: GET /monitor/active/{monitor_id}
- Get Monitor's Operational Status: GET /monitor/status/{monitor_id}

## Contributing

Contributions to this project are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear, descriptive messages.
4. Push your branch and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
