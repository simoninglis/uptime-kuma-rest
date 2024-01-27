import os
import logging
from flask import Flask, jsonify, request
from uptime_kuma_api import UptimeKumaApi
from dotenv import load_dotenv
from flasgger import Swagger, swag_from

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
swagger = Swagger(app)

# Read configuration from environment variables
username = os.getenv('UPTIME_KUMA_USERNAME')
password = os.getenv('UPTIME_KUMA_PASSWORD')
base_url = os.getenv('UPTIME_KUMA_BASE_URL')

# Initialize the Uptime Kuma API client
uptime_kuma_client = UptimeKumaApi(base_url)
# Authenticate with the Uptime Kuma API
uptime_kuma_client.login(username, password)

@app.route('/')
def index():
    logger.info("Received request for index")
    return "Uptime Kuma API Wrapper"

@app.route('/monitors', methods=['GET'])
@swag_from('docs/monitors.yml')
def list_monitors():
    """Endpoint to list all monitors with ID, name, and active status."""
    tag = request.args.get('tag')  # Get the 'tag' query parameter
    try:
        monitors = uptime_kuma_client.get_monitors()
        simplified_monitors = []
        for monitor in monitors:
            # If a tag is specified and the monitor doesn't have this tag, skip it
            if tag and tag not in monitor['tags']:
                continue
            simplified_monitor = {
                'id': monitor['id'],
                'name': monitor['name'],
                'active': monitor['active']
            }
            simplified_monitors.append(simplified_monitor)
        return jsonify(simplified_monitors), 200
    except Exception as e:
        logger.error(f"Failed to list monitors: {e}")
        return jsonify({"error": "Failed to list monitors"}), 500

    
@app.route('/monitor/<int:monitor_id>', methods=['GET'])
@swag_from('docs/monitor_details.yml')
def get_monitor_details(monitor_id):
    """Endpoint to get details for a specific monitor by its ID."""
    try:
        monitor_details = uptime_kuma_client.get_monitor(monitor_id)
        return jsonify(monitor_details), 200
    except Exception as e:
        logger.error(f"Failed to get monitor details for ID {monitor_id}: {e}")
        return jsonify({"error": "Failed to get monitor details"}), 500

@app.route('/monitor/active/<int:monitor_id>', methods=['GET'])
@swag_from('docs/is_monitor_active.yml')
def is_monitor_active(monitor_id):
    """Endpoint to check if a specific monitor is active."""
    try:
        monitor_details = uptime_kuma_client.get_monitor(monitor_id)
        is_active = monitor_details.get('active', False)  # Assuming 'active' is a key in the monitor details
        return jsonify({"active": is_active}), 200
    except Exception as e:
        logger.error(f"Failed to get monitor active status for ID {monitor_id}: {e}")
        return jsonify({"error": "Failed to get monitor active status"}), 500


@app.route('/monitor/status/<int:monitor_id>', methods=['GET'])
@swag_from('docs/get_monitor_status.yml')
def get_monitor_status(monitor_id):
    """Endpoint to get the status of a specific monitor."""
    try:
        monitor_details = uptime_kuma_client.get_monitor(monitor_id)
        status = monitor_details.get('status', 'Unknown')  # Assuming 'status' is a key in the monitor details
        return jsonify({"status": status}), 200
    except Exception as e:
        logger.error(f"Failed to get monitor status for ID {monitor_id}: {e}")
        return jsonify({"error": "Failed to get monitor status"}), 500


@app.route('/monitor/resume/<int:monitor_id>', methods=['POST'])
@swag_from('docs/resume_monitor.yml')
def resume_monitor(monitor_id):
    """Endpoint to resume a monitor by its ID."""
    logger.info(f"Resuming monitor with ID: {monitor_id}")
    result = uptime_kuma_client.resume_monitor(monitor_id)
    return jsonify(result)

@app.route('/monitor/pause/<int:monitor_id>', methods=['POST'])
@swag_from('docs/pause_monitor.yml')
def pause_monitor(monitor_id):
    """Endpoint to pause a monitor by its ID."""
    logger.info(f"Pausing monitor with ID: {monitor_id}")
    result = uptime_kuma_client.pause_monitor(monitor_id)
    return jsonify(result)

if __name__ == '__main__':
    logger.info("Starting the Uptime Kuma API Wrapper")
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
