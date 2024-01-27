# Getting Started with Uptime Kuma API Wrapper

This guide will walk you through the process of setting up the Uptime Kuma API Wrapper on your system. Follow these steps to install the wrapper, configure it with your Uptime Kuma instance, and start using it to manage your monitors.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed and set up:

- Docker: If you prefer to run the API Wrapper in a Docker container.
- Python 3.8 or newer: If you plan to run the API Wrapper directly on your system.
- An Uptime Kuma Instance: The API Wrapper is designed to interact with Uptime Kuma, so you'll need an existing Uptime Kuma instance.

## Installation

You can install and run the Uptime Kuma API Wrapper using Docker or directly on your local system.

### Using Docker

1. Clone the repository to your local machine:
   git clone https://example.com/uptime-kuma-api-wrapper.git
   cd uptime-kuma-api-wrapper

2. Build the Docker image:
   docker build -t uptime-kuma-api-wrapper .

3. Run the Docker container, replacing the placeholders with your actual Uptime Kuma credentials and the URL of your Uptime Kuma instance:
   docker run -d -p 5000:5000 --env UPTIME_KUMA_USERNAME=your_username --env UPTIME_KUMA_PASSWORD=your_password --env UPTIME_KUMA_BASE_URL=your_uptime_kuma_instance_url uptime-kuma-api-wrapper

### Running Locally

1. Ensure Python 3.8+ is installed on your system.

2. Clone the repository and navigate into the project directory:
   git clone https://example.com/uptime-kuma-api-wrapper.git
   cd uptime-kuma-api-wrapper

3. Install the required dependencies:
   pip install -r requirements.txt

4. Set up your environment variables by creating a .env file in the project root with your Uptime Kuma credentials and URL:
   UPTIME_KUMA_USERNAME=your_username
   UPTIME_KUMA_PASSWORD=your_password
   UPTIME_KUMA_BASE_URL=http://your-uptime-kuma-instance.com

5. Start the Flask application:
   python app.py

The application will start on http://localhost:5000/, and you can begin interacting with your Uptime Kuma monitors through the API.

## Next Steps

Now that you have the Uptime Kuma API Wrapper running, you might want to:

- Explore the Usage section to learn how to interact with the API.
- Check the Development section if you're interested in contributing to the project.
