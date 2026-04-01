from schedule_manager_ui import ScheduleManager

default_manager_path = "/schedule-manager-ui"


def test_endpoint(client, schedule_manager):
    response = client.get(default_manager_path)
    assert response.status_code == 200


def test_custom_path(client, app, scheduler):
    schedule_manager_custom_path = ScheduleManager(app, scheduler, path='/custom-url')
    response = client.get(schedule_manager_custom_path.HOME_PATH)
    assert response.status_code == 200

    response = client.get(default_manager_path)
    assert response.status_code == 404


def test_custom_db_url(app, scheduler):
    sm = ScheduleManager(app, scheduler, db_url='sqlite:///:memory:')
    assert sm.engine is not None


def test_default_db_url(schedule_manager):
    assert 'apscheduler_events.db' in str(schedule_manager.engine.url)
