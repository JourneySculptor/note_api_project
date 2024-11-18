# Note API Project

A simple note-taking REST API built with Flask.

## Features

- Create new notes
- Retrieve all notes
- Retrieve specific notes by ID
- Delete specific notes by ID (New Feature!)

## How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/JourneySculptor/note_api_project.git
    ```

2. Navigate to the project folder:

    ```bash
    cd note_api_project
    ```

3. Set up a virtual environment:

    **For Mac/Linux:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

    **For Windows:**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

4. Install dependencies:

    ```bash
    pip install flask
    ```

5. Run the app:

    ```bash
    python app.py
    ```

6. Access the API locally at:

    ```
    http://127.0.0.1:5000/
    ```

## Endpoints

### 1. Create a New Note

- **URL**: `POST /notes`
- **Request Body (JSON)**:

    ```json
    {
        "title": "My First Note",
        "content": "This is the content of my first note."
    }
    ```

- **Response**:

    ```json
    {
        "id": 1,
        "title": "My First Note",
        "content": "This is the content of my first note."
    }
    ```

### 2. Retrieve All Notes

- **URL**: `GET /notes`
- **Response**:

    ```json
    {
        "notes": [
            {
                "id": 1,
                "title": "My First Note",
                "content": "This is the content of my first note."
            }
        ]
    }
    ```

### 3. Retrieve a Specific Note by ID

- **URL**: `GET /notes/<id>`
- **Response (200)**:

    ```json
    {
        "id": 1,
        "title": "My First Note",
        "content": "This is the content of my first note."
    }
    ```

- **Response (404)**:

    ```json
    {
        "message": "Note not found"
    }
    ```

### 4. Delete a Specific Note by ID

- **URL**: `DELETE /notes/<id>`
- **Response (200)**:

    ```json
    {
        "message": "Note deleted successfully"
    }
    ```

- **Response (404)**:

    ```json
    {
        "message": "Note not found"
    }
    ```

## Project Structure

```plaintext
note_api_project/
├── app.py             # Main application file
├── requests.http      # HTTP request examples for testing
└── README.md          # Project documentation
 ```

## Project Structure
This project is licensed under the MIT License.
