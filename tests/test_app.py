import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    app = flask_app
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_list_monitors_integration(client):
    """Integration test for listing monitors against the real Uptime Kuma instance."""
    response = client.get('/monitors')
    assert response.status_code == 200
    # Depending on the expected structure of the monitors list, you might want to add more assertions here
    # For example, to check if the response is a list:
    assert isinstance(response.json, list)
    # And perhaps some basic checks on the list items
    if response.json:
        assert 'id' in response.json[0]
        assert 'name' in response.json[0]


def test_list_monitors_with_tag(client):
    """Integration test for listing monitors with a specific tag against the real Uptime Kuma instance."""
    response = client.get('/monitors?tag=Application')
    assert response.status_code == 200
    # Depending on the expected structure of the monitors list, you might want to add more assertions here
    # For example, to check if the response is a list:
    assert isinstance(response.json, list)
    # And perhaps some basic checks on the list items
    if response.json:
        assert 'id' in response.json[0]
        assert 'name' in response.json[0]
        # Check if the returned monitors have the 'Application' tag
        assert 'Application' in response.json[0]['tags']


def test_pause_resume_monitor(client):
    # Get the list of monitors and select the first one
    response = client.get('/monitors')
    assert response.status_code == 200
    monitors = response.json
    assert monitors, "No monitors found. Ensure Uptime Kuma has at least one monitor for this test."
    first_monitor = monitors[0]

    # Pause the first monitor
    pause_response = client.post(f'/monitor/pause/{first_monitor["id"]}')
    assert pause_response.status_code == 200, "Failed to pause the monitor."

    # Check if the monitor is active (should be False for paused)
    active_response = client.get(f'/monitor/active/{first_monitor["id"]}')
    assert active_response.status_code == 200, "Failed to check if monitor is active."
    assert not active_response.json['active'], "Monitor was not paused successfully."

    # Resume the first monitor
    resume_response = client.post(f'/monitor/resume/{first_monitor["id"]}')
    assert resume_response.status_code == 200, "Failed to resume the monitor."

    # Check if the monitor is active again (should be True for resumed)
    active_response = client.get(f'/monitor/active/{first_monitor["id"]}')
    assert active_response.status_code == 200, "Failed to check if monitor is active after resuming."
    assert active_response.json['active'], "Monitor was not resumed successfully."
