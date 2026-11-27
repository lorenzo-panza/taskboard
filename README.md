# taskboard
DevSecOps Lab - TaskBoard v0.1

# TaskBoard v0.1

## Purpose

TaskBoard is a REST API for managing tasks, developed
as part of the ESIEE Paris DevSecOps lab.

The application supports creating, listing, retrieving,
updating and deleting tasks using in-memory storage.

## Requirements

- Python 3.11+
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/lorenzo-panza/taskboard.git
cd taskboard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows (CMD):

```cmd
.venv\Scripts\activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | /tasks | Create a task |
| GET | /tasks | List all tasks |
| GET | /tasks/{task_id} | Get a task |
| PATCH | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |
| GET | /health | Check API health |

## Tests

```bash
pytest -v
```

Automated tests will be implemented in Step 2.

## Environment variables

Copy `.env.example` to `.env`.

Never commit the `.env` file or real secrets.

The current version uses in-memory storage and
does not require a database.

## Project structure

```text
taskboard/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── tasks.py
├── tests/
│   ├── __init__.py
│   └── test_tasks.py
├── docs/
├── .gitignore
├── .env.example
├── README.md
└── requirements.txt
```

## Known limitations

- Tasks are lost when the server restarts.
- Input validation is currently limited.
- Authentication and authorization are not implemented.
- Input validation and automated tests will be added in PR #2.
