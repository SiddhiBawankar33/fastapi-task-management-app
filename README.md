# FastAPI Task Management App

A RESTful API built with **Python, FastAPI, PostgreSQL, and SQLAlchemy** for managing tasks and user accounts. This project is being developed to practise backend development, API design, database integration, and authentication.

## 🚀 Features

### Task Management

- Create a task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task

### User Management and Authentication

- User registration
- OAuth2-based authentication implementation
- Password hashing with `pwdlib` and Argon2, if configured in the application
- JWT access tokens, if implemented and enabled

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** OAuth2
- **Password Hashing:** pwdlib with Argon2, if used
- **Token Management:** JWT with PyJWT, if used

## 📁 Project Structure

```text
task_management_app/
├── src/
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   ├── user/
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── dtos.py
│   │   ├── models.py
│   │   └── router.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── db.py
│       ├── helpers.py
│       ├── constant.py
│       └── settings.py
│
├── main.py
├── requirement.txt
├── .gitignore
└── README.md
```

### Directory Overview

- **`src/tasks/`** — Task-related routes, request/response DTOs, database models, and controller logic.
- **`src/user/`** — User-related routes, DTOs, models, and controller logic, including registration and authentication functionality.
- **`src/utils/`** — Shared utilities, database configuration, application settings, and constants.
- **`main.py`** — Application entry point where the FastAPI application is initialized and routes are registered.
- **`requirement.txt`** — Python dependencies required to run the project.
- **`.gitignore`** — Specifies files and folders Git should exclude from version control.

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/SiddhiBawankar33/fastapi-task-management-app.git
cd fastapi-task-management-app
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

If your dependency file is named `requirement.txt`:

```powershell
pip install -r requirement.txt
```

If you rename it to `requirements.txt`, use that filename instead.

### 4. Configure environment variables

Create a local `.env` file in the project root and add the configuration required by your application, such as your PostgreSQL connection URL and authentication secret.

Use placeholder values in documentation. Never commit real passwords, database credentials, or signing secrets to GitHub.

### 5. Run the application

```powershell
fastapi dev main.py
```

Open the interactive API documentation at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Testing the API

Use the interactive Swagger UI at `/docs` or a tool such as Postman to test your endpoints.

Verify task creation, retrieval, updates, deletion, and user authentication according to the routes implemented in your application.

## 🔒 Security Notes

- Store password hashes rather than plain-text passwords.
- Keep credentials and signing secrets in environment variables.
- Validate request data and handle errors appropriately.
- Protect private endpoints with authentication and authorization checks.

## 📌 Project Status

**Work in Progress**

This project is being developed incrementally. Features, tests, and documentation will be updated as the implementation evolves.

## 👩‍💻 Author

**Siddhi Bawankar**

GitHub: [@SiddhiBawankar33](https://github.com/SiddhiBawankar33)
