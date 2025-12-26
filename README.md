# Python Backend API (FastAPI)

A modular **Python backend application** built with **FastAPI**, demonstrating clean API design, authentication, database integration, and file handling.  
This project is suitable for learning, extension, and portfolio use.

---

## 🚀 Features

- FastAPI-based REST APIs
- Async database support with SQLAlchemy / SQLModel
- JWT-based authentication
- User management
- File uploads
- Image handling with ImageKit
- Environment-based configuration
- Clean, scalable project structure

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **SQLAlchemy / SQLModel**
- **FastAPI Users (JWT Auth)**
- **SQLite (default, async)**
- **Pydantic**
- **ImageKit**
- **dotenv**

---

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py            # Application entry point
│   ├── db/                # Database configuration
│   ├── models/            # Database models
│   ├── schemas/           # Pydantic schemas
│   ├── routers/           # API routes
│   ├── users/             # Authentication & user logic
│   └── images/            # Image upload logic
│
├── requirements.txt
├── .gitignore
└── README.md
```

# Clone the repository

- git clone https://github.com/SujithGowdru/Python-FastAPI.git
- cd your-repo-name

# Install dependencies

- Using pip : pip install -r requirements.txt

- OR

- pip install uv
- uv pip install -r requirements.txt

# Run the Application

- uv run main.py

# Access the API

- • API Base URL: http://127.0.0.1:8000
  • Swagger UI: http://127.0.0.1:8000/docs
  • ReDoc: http://127.0.0.1:8000/redoc
