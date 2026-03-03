# CodeCraftHub

A Simple Personalized Learning Platform for Developers

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

---

## Project Overview

**CodeCraftHub** is a beginner-friendly REST API built with Python and Flask. It lets you track developer courses you want to learn — no database required, just a JSON file.

### What You'll Learn

- REST API basics — what REST is and how it works
- HTTP methods — GET, POST, PUT, DELETE
- Flask framework — building web apps with Python
- JSON file storage — reading and writing persistent data
- Error handling — returning meaningful error messages
- API design — structuring endpoints logically

### What is CRUD?

| Operation | HTTP Method | Description         |
|-----------|-------------|---------------------|
| Create    | POST        | Add a new course    |
| Read      | GET         | View courses        |
| Update    | PUT         | Modify a course     |
| Delete    | DELETE      | Remove a course     |

---

## Features

- Add, view, update, and delete courses
- Filter courses by status
- Auto-generated IDs and timestamps
- Input validation with clear error messages
- JSON file storage — no database setup needed
- Automatic creation of `data/courses.json` on first run

### Course Fields

| Field         | Type    | Description                                          |
|---------------|---------|------------------------------------------------------|
| `id`          | Integer | Unique identifier (auto-generated)                   |
| `name`        | String  | Course name (required)                               |
| `description` | String  | Course description (required)                        |
| `target_date` | String  | Target completion date in `YYYY-MM-DD` format        |
| `status`      | String  | `Not Started`, `In Progress`, or `Completed`         |
| `created_at`  | String  | ISO timestamp, auto-generated on creation            |

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- curl or a REST client (Postman, Insomnia, etc.)

---

## Installation

**Step 1 — Create the project directory**

```bash
mkdir codecrafthub
cd codecrafthub
```

**Step 2 — Add project files**

Place `app.py`, `requirements.txt`, and the `data/` folder in this directory.

**Step 3 — Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python app.py
```

You should see:

```
- CodeCraftHub API is starting...
- Data will be stored in: /path/to/data/courses.json
- API will be available at: http://localhost:5000
```

---

## API Endpoints

| Method | Endpoint                  | Description             |
|--------|---------------------------|-------------------------|
| POST   | `/api/courses`            | Create a new course     |
| GET    | `/api/courses`            | Get all courses         |
| GET    | `/api/courses/<id>`       | Get a specific course   |
| PUT    | `/api/courses/<id>`       | Update a course         |
| DELETE | `/api/courses/<id>`       | Delete a course         |

---

## Testing the API

Open a **new terminal window** while the server is running.

### Add a course (POST)

```bash
curl -X POST http://localhost:5000/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python fundamentals",
    "target_date": "2025-12-31",
    "status": "Not Started"
  }'
```

Expected response (201):

```json
{
    "message": "Course created successfully",
    "course": {
        "id": 1,
        "name": "Python Basics",
        "description": "Learn Python fundamentals",
        "target_date": "2025-12-31",
        "status": "Not Started",
        "created_at": "2025-01-15T10:30:45"
    }
}
```

### Get all courses (GET)

```bash
curl http://localhost:5000/api/courses
```

### Get a specific course (GET)

```bash
curl http://localhost:5000/api/courses/1
```

### Update a course (PUT)

```bash
curl -X PUT http://localhost:5000/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{
    "status": "In Progress"
  }'
```

### Delete a course (DELETE)

```bash
curl -X DELETE http://localhost:5000/api/courses/1
```

---

## Error Handling

The API returns structured errors for common problems:

| Scenario                  | Status Code | Example Response                                      |
|---------------------------|-------------|-------------------------------------------------------|
| Missing required field    | 400         | `{"error": "Missing required fields: name"}`          |
| Invalid status value      | 400         | `{"error": "status must be one of: Not Started, ..."}`|
| Invalid date format       | 400         | `{"error": "target_date must be in YYYY-MM-DD format"}`|
| Course not found          | 404         | `{"error": "Course with id 99 not found"}`            |
| File read/write error     | 500         | `{"error": "Could not read data file"}`               |

---

## Project Structure

```
codecrafthub/
├── app.py              # Flask application — all routes and helpers
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── data/
    └── courses.json    # Persistent course storage (auto-created)
```

### Key Functions in `app.py`

| Function                  | Purpose                                          |
|---------------------------|--------------------------------------------------|
| `ensure_data_file_exists` | Creates `data/` and `courses.json` on first run  |
| `read_data`               | Reads and parses the JSON file                   |
| `write_data`              | Serialises and saves data back to the JSON file  |
| `find_course_by_id`       | Locates a course by its integer ID               |
| `validate_course_data`    | Checks required fields, formats, and status      |

---

## Troubleshooting

**Port 5000 already in use**

```bash
# macOS/Linux — find and kill the process on port 5000
lsof -ti:5000 | xargs kill -9
```

**`ModuleNotFoundError: No module named 'flask'`**

```bash
pip install -r requirements.txt
```

**JSON file is corrupted**

Delete `data/courses.json` and restart the app — it will be recreated automatically.

**`curl` not recognised on Windows**

Use [Git Bash](https://gitforwindows.org/) or [Postman](https://www.postman.com/) instead.

---

## Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [REST API Tutorial](https://restfulapi.net/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [JSON Format Guide](https://www.json.org/json-en.html)

---

## License

This project is licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for details.
