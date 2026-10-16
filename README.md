# FastAPI Task Management API

A RESTful Task Management API built with **Python, FastAPI, PostgreSQL, and SQLAlchemy**. The application supports user registration, secure authentication, and task management with database persistence and user-specific task associations.

This project was developed as a hands-on backend learning project covering REST API development, database integration, authentication and authorization, database migrations, email utilities, and API testing with Postman.

## 🚀 Features

### Task Management

- Create new tasks for the authenticated user.
- Retrieve all tasks associated with the authenticated user.
- Retrieve a task by its ID.
- Update existing task details.
- Delete tasks.
- Store task information in PostgreSQL.

### User Management and Authentication

- User registration and login.
- Password hashing using `pwdlib`.
- JWT-based access tokens using PyJWT.
- Authentication of protected endpoints.
- Dependency-based authentication using FastAPI's `Depends`.
- Association of tasks with their respective users.

### Database and Migrations

- PostgreSQL database integration.
- SQLAlchemy ORM for database operations.
- Separate database models for users and tasks.
- Database session management and dependency injection.
- Alembic migrations for tracking database schema changes.
- User–task relationship through a foreign key.

### Email and Background Processing

- Email-sending utility in `src/utils/mail.py`.
- Email configuration for application email functionality.
- FastAPI background-task support for running supported tasks without blocking the immediate response.

## 🛠️ Tech Stack

| Technology    | Purpose                                 |
| ------------- | --------------------------------------- |
| Python        | Programming language                    |
| FastAPI       | REST API framework                      |
| PostgreSQL    | Relational database                     |
| SQLAlchemy    | ORM and database operations             |
| Pydantic      | Request validation and response schemas |
| PyJWT         | JWT token generation and validation     |
| pwdlib        | Password hashing and verification       |
| Alembic       | Database schema migrations              |
| python-dotenv | Environment variable loading            |
| Postman       | API testing                             |

## 📁 Project Structure

```text
fastapi-task-management-app/
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
│       ├── settings.py
│       └── mail.py
│
├── migrations/
│   ├── versions/
│   │   └── 40073df74e1b_add_user_id_to_tasks.py
│   ├── env.py
│   └── script.py.mako
│
├── main.py
├── requirement.txt
├── alembic.ini
├── .gitignore
└── README.md
```

### Directory Overview

- **`src/tasks/`** — Task-related API routes, request and response schemas, database models, and business logic.
- **`src/user/`** — User registration, login, authentication-related functionality, schemas, and models.
- **`src/utils/`** — Shared utilities for database connections, authentication helpers, application settings, constants, and email functionality.
- **`migrations/`** — Alembic configuration scripts and migration versions used to manage database schema changes.
- **`main.py`** — Initializes the FastAPI application and registers API routers.
- **`alembic.ini`** — Alembic configuration file. Database credentials are loaded securely through environment configuration rather than committed as plain text.
- **`requirement.txt`** — Python package dependencies.
- **`.gitignore`** — Excludes environment files, virtual environments, Python cache files, and other files from version control.

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or a compatible version supported by the installed dependencies.
- PostgreSQL.
- Git.
- Postman (optional, for API testing).

### 1. Clone the repository

```bash
git clone https://github.com/SiddhiBawankar33/fastapi-task-management-app.git
cd fastapi-task-management-app
```

### 2. Create and activate a virtual environment

For Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirement.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root. Configure the variables expected by `src/utils/settings.py` and `migrations/env.py`.

For example, if your application uses `DB_CONNECTION` for the database URL:

```env
DB_CONNECTION=postgresql://USERNAME:PASSWORD@localhost:5432/DATABASE_NAME
SECRET_KEY=replace_with_a_secure_random_secret
ALGORITHM=HS256
```

Replace the placeholders with your own local configuration. Include any additional email settings required by your email utility.

**Security:** Never commit `.env`, actual database credentials, email app passwords, or signing secrets to GitHub. The `.env` file should remain excluded by `.gitignore`.

### 5. Set up the database

Create a PostgreSQL database and ensure the database connection settings are correct.

Apply the available Alembic migrations:

```powershell
alembic upgrade head
```

To check the current migration revision:

```powershell
alembic current
```

### 6. Run the application

```powershell
fastapi dev main.py
```

The API should be available at:

- **Interactive API documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative API documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 API Endpoints

The following task routes are defined in the task router. All task operations require authentication.

| Method | Endpoint                       | Description                       |
| ------ | ------------------------------ | --------------------------------- |
| POST   | `/tasks/create`                | Create a task                     |
| GET    | `/tasks/all_tasks`             | Retrieve the current user's tasks |
| GET    | `/tasks/get_task/{task_id}`    | Retrieve a task by ID             |
| PUT    | `/tasks/update_task/{task_id}` | Update a task                     |
| DELETE | `/tasks/delete_task/{task_id}` | Delete a task                     |

User registration and login endpoints are defined in the user router. Their exact paths depend on the prefixes configured in `src/user/router.py` and `main.py`.

### Authentication Flow

1. Register a user through the registration endpoint.
2. Log in using the registered credentials.
3. Obtain the JWT access token from the login response.
4. Include the token in the `Authorization` header when accessing protected routes.

Example header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Use a valid token generated by your application. Tokens may expire according to the configured expiration time.

## 🧪 Testing

The API was tested using **Postman**.

Testing covered the implemented task CRUD operations and authentication flow, including:

- User registration and login.
- JWT token generation and validation.
- Access to protected endpoints.
- Task creation and retrieval.
- Task updates and deletion.
- PostgreSQL persistence.
- Database migration status.

You can also use the interactive Swagger UI at `/docs` to explore and test the available endpoints.

## 🔒 Security Considerations

- Store password hashes rather than plain-text passwords.
- Keep database credentials, email passwords, and signing secrets in environment variables.
- Protect private endpoints using authentication and authorization.
- Validate incoming request data using Pydantic schemas.
- Ensure users can only access or modify their own tasks.
- Keep environment files and virtual environments out of version control.
- Use HTTPS and appropriately managed secrets when deploying the application.

## 📚 What I Learned

Through this project, I gained practical experience with:

- Designing REST APIs using FastAPI.
- Implementing CRUD operations.
- Organizing a backend application into routers, controllers, schemas, and models.
- Connecting PostgreSQL with SQLAlchemy.
- Managing database sessions and dependencies.
- Implementing password hashing and JWT authentication.
- Associating database records with authenticated users.
- Managing schema changes using Alembic.
- Working with email utilities and background tasks.
- Testing APIs and debugging backend issues using Postman.

## 📌 Project Status

**Completed — Local development and Postman testing finished.**

This project represents my hands-on practice in backend development using FastAPI, PostgreSQL, SQLAlchemy, authentication, and database migrations.

## 👩‍💻 Author

**Siddhi Bawankar**

GitHub: [@SiddhiBawankar33](https://github.com/SiddhiBawankar33)

Project Repository: [FastAPI Task Management API](https://github.com/SiddhiBawankar33/fastapi-task-management-app)
