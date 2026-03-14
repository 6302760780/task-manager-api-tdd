# Task Manager API (TDD + AI Assisted)

## Overview

This project is a simple Task Manager API built using Python and FastAPI following a Test-Driven Development (TDD) workflow.

The goal of this project is to demonstrate:

- writing tests before implementing features
- using AI tools as development assistants
- building clean and maintainable API code
- documenting design decisions and tradeoffs

The API allows users to:

- create tasks
- view tasks
- delete tasks

---

# Tech Stack

Python  
FastAPI  
Pytest  
Uvicorn  

---

# Project Structure
task-manager-api
│
├── app
│ ├── main.py
│ ├── models.py
│ ├── routes.py
│ └── store.py
│
├── tests
│ ├── conftest.py
│ ├── test_create_task.py
│ ├── test_get_tasks.py
│ ├── test_delete_task.py
│ └── test_validation.py
│
├── README.md
├── AI_USAGE.md
├── Dockerfile
├── requirements.txt
└── .gitignore

---

# How to Run the Application

### Step 1 — Navigate to the project folder
cd task-manager-api
### Step 2 — Run the API server
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload
You should see something similar to:
Uvicorn running on http://127.0.0.1:8000
### Step 3 — Open API documentation
Open your browser and go to:
http://127.0.0.1:8000/docs

This page allows you to interact with the API.
# API Endpoints
## Create Task
POST /tasks
Example request body:
{
"title": "My task"
}
## Get Tasks
GET /tasks
Returns a list of all tasks.
## Delete Task
DELETE /tasks/{task_id}
Deletes the task with the specified ID.
# Running the Tests
To run the automated tests:
.\venv\Scripts\python.exe -m pytest
Expected output:
4 passed

The tests verify:

- task creation
- listing tasks
- deleting tasks
- validation for empty task titles

# Design Decisions

### FastAPI

FastAPI was chosen because it provides:

- automatic API documentation
- built-in validation
- simple and readable syntax

### In-Memory Storage

Tasks are stored in memory rather than a database to keep the project simple and focused on demonstrating the TDD workflow.

### Test-Driven Development

Tests were written first for the core features:

1. create task
2. list tasks
3. delete task
4. validation rules

The implementation was then written to satisfy those tests.

# Assumptions and Tradeoffs

- tasks are not persisted between server restarts
- authentication was not implemented
- no database integration was added

These decisions were made to keep the focus on demonstrating the TDD process.

# What I Would Improve With More Time

- add persistent storage (SQLite or PostgreSQL)
- add update and complete-task endpoints
- add CI pipeline for automated testing
- add structured logging



