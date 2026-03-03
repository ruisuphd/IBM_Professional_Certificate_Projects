"""
CodeCraftHub - A Simple Personalized Learning Platform
=======================================================

A beginner-friendly REST API for tracking developer courses.
Demonstrates basic Flask concepts and JSON file storage.

License: Apache 2.0
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import json
import os

# ---------------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DATA_FILE = os.path.join(DATA_DIR, 'courses.json')

VALID_STATUSES = ['Not Started', 'In Progress', 'Completed']

# ---------------------------------------------------------------------------
# JSON file helpers
# ---------------------------------------------------------------------------

def ensure_data_file_exists():
    """Create data directory and courses.json if they don't exist."""
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        if not os.path.exists(DATA_FILE):
            default_data = {"courses": [], "next_id": 1}
            with open(DATA_FILE, 'w') as f:
                json.dump(default_data, f, indent=4)

        return True
    except Exception as e:
        print(f"Error creating data file: {e}")
        return False


def read_data():
    """Read all data from the JSON file. Returns None on error."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Data file not found at {DATA_FILE}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in data file - {e}")
        return None
    except Exception as e:
        print(f"Error reading data file: {e}")
        return None


def write_data(data):
    """Write data dict to the JSON file. Returns True on success."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error writing data file: {e}")
        return False


def find_course_by_id(courses, course_id):
    """Return (course_dict, index) for matching id, or (None, -1) if not found."""
    for index, course in enumerate(courses):
        if course['id'] == course_id:
            return course, index
    return None, -1


def validate_course_data(data, require_all_fields=True):
    """
    Validate incoming course payload.

    Args:
        data: dict from request JSON
        require_all_fields: True for POST/PUT; False for PATCH-style partial updates

    Returns:
        (is_valid: bool, error_message: str | None)
    """
    if not data:
        return False, "Request body must be valid JSON"

    if require_all_fields:
        required = ['name', 'description', 'target_date', 'status']
        missing = [f for f in required if f not in data]
        if missing:
            return False, f"Missing required fields: {', '.join(missing)}"

    if 'name' in data and not str(data['name']).strip():
        return False, "Course name cannot be empty"

    if 'description' in data and not str(data['description']).strip():
        return False, "Course description cannot be empty"

    if 'target_date' in data:
        try:
            datetime.strptime(data['target_date'], '%Y-%m-%d')
        except ValueError:
            return False, "target_date must be in YYYY-MM-DD format"

    if 'status' in data and data['status'] not in VALID_STATUSES:
        return False, f"status must be one of: {', '.join(VALID_STATUSES)}"

    return True, None

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'dashboard.html')


@app.route('/api/courses', methods=['POST'])
def create_course():
    """Add a new course."""
    data = request.get_json(silent=True)

    is_valid, error = validate_course_data(data, require_all_fields=True)
    if not is_valid:
        return jsonify({"error": error}), 400

    db = read_data()
    if db is None:
        return jsonify({"error": "Could not read data file"}), 500

    course = {
        "id": db['next_id'],
        "name": data['name'].strip(),
        "description": data['description'].strip(),
        "target_date": data['target_date'],
        "status": data['status'],
        "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    }

    db['courses'].append(course)
    db['next_id'] += 1

    if not write_data(db):
        return jsonify({"error": "Could not save data"}), 500

    return jsonify({"message": "Course created successfully", "course": course}), 201


@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    """Return all courses."""
    db = read_data()
    if db is None:
        return jsonify({"error": "Could not read data file"}), 500

    return jsonify({
        "message": "Courses retrieved successfully",
        "count": len(db['courses']),
        "courses": db['courses']
    }), 200


@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """Return a single course by ID."""
    db = read_data()
    if db is None:
        return jsonify({"error": "Could not read data file"}), 500

    course, _ = find_course_by_id(db['courses'], course_id)
    if course is None:
        return jsonify({"error": f"Course with id {course_id} not found"}), 404

    return jsonify({"message": "Course retrieved successfully", "course": course}), 200


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    """Update one or more fields of an existing course."""
    data = request.get_json(silent=True)

    is_valid, error = validate_course_data(data, require_all_fields=False)
    if not is_valid:
        return jsonify({"error": error}), 400

    db = read_data()
    if db is None:
        return jsonify({"error": "Could not read data file"}), 500

    course, index = find_course_by_id(db['courses'], course_id)
    if course is None:
        return jsonify({"error": f"Course with id {course_id} not found"}), 404

    updatable = ['name', 'description', 'target_date', 'status']
    for field in updatable:
        if field in data:
            value = data[field]
            db['courses'][index][field] = value.strip() if isinstance(value, str) else value

    if not write_data(db):
        return jsonify({"error": "Could not save data"}), 500

    return jsonify({
        "message": "Course updated successfully",
        "course": db['courses'][index]
    }), 200


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    """Delete a course by ID."""
    db = read_data()
    if db is None:
        return jsonify({"error": "Could not read data file"}), 500

    course, index = find_course_by_id(db['courses'], course_id)
    if course is None:
        return jsonify({"error": f"Course with id {course_id} not found"}), 404

    db['courses'].pop(index)

    if not write_data(db):
        return jsonify({"error": "Could not save data"}), 500

    return jsonify({"message": f"Course '{course['name']}' deleted successfully"}), 200


# ---------------------------------------------------------------------------
# Startup
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    print("- CodeCraftHub API is starting...")
    print(f"- Data will be stored in: {DATA_FILE}")
    print("- API will be available at: http://localhost:5000")

    if not ensure_data_file_exists():
        print("ERROR: Could not create data file. Exiting.")
        exit(1)

    app.run(debug=True, host='0.0.0.0', port=5000)
