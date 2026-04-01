# schedule-manager-ui

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Example](#example)
   
## Description
Web UI for seamless interaction with APScheduler job schedulers, ready to use out of the box. 
> [![Downloads](https://pepy.tech/badge/schedule-manager-ui)](https://pepy.tech/project/schedule-manager-ui) 

## Installation
You can use `pip` to install. 
```bash
pip install schedule-manager-ui
```

## Usage
```python
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from schedule_manager_ui import ScheduleManager

app = Flask(__name__)
scheduler = BackgroundScheduler()
sm = ScheduleManager(app, scheduler)
```

## Configuration

`ScheduleManager` accepts the following constructor parameters:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `app` | `Flask` | *(required)* | The Flask application instance. |
| `scheduler` | `BaseScheduler` | *(required)* | The APScheduler scheduler instance. |
| `path` | `str` | `'/schedule-manager-ui'` | URL path prefix for the manager UI. |
| `require_authentication` | `bool` | `True` | Whether to require an API key for job toggle requests. |
| `apikey` | `str` | `None` | API key for authentication. Falls back to the `SM_UI_APIKEY` environment variable when not provided. |
| `db_url` | `str` | `'sqlite:///apscheduler_events.db'` | SQLAlchemy database URL used to store job execution events. |

### Environment Variables

| Variable | Description |
|---|---|
| `SM_UI_APIKEY` | API key used for authentication when `require_authentication=True` and `apikey` is not passed directly. |
| `TZ` | Timezone name (e.g. `Europe/Warsaw`) used for event timestamps. Falls back to the system timezone when not set. |

### Examples

**Disable authentication** (development only):
```python
sm = ScheduleManager(app, scheduler, require_authentication=False)
```

**Custom UI path**:
```python
sm = ScheduleManager(app, scheduler, path='/jobs')
```

**Provide API key explicitly**:
```python
sm = ScheduleManager(app, scheduler, apikey='my-secret-key')
```

**Use a PostgreSQL database for event storage**:
```python
sm = ScheduleManager(app, scheduler, db_url='postgresql://user:password@localhost/mydb')
```

**Use an in-memory SQLite database** (useful for testing):
```python
sm = ScheduleManager(app, scheduler, db_url='sqlite:///:memory:')
```

## Example
Following interface can be accessed via `/schedule-manager-ui`.

![image](https://github.com/user-attachments/assets/9d2df283-242e-46e5-b693-e1708517e377)
