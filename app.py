from flask import Flask, request, jsonify

app = Flask(__name__)

# List to store notes
notes = []

@app.route('/notes', methods=['POST'])
def create_note():
    """
    Create a new note.

    Request body:
    {
        "title": "Note title",
        "content": "Note content"
    }

    Response:
    {
        "id": 1,
        "title": "Note title",
        "content": "Note content"
    }
    """
    data = request.get_json()
    new_note = {
        "id": len(notes) + 1,
        "title": data['title'],
        "content": data['content']
    }
    notes.append(new_note)
    return jsonify(new_note), 201

@app.route('/notes', methods=['GET'])
def get_notes():
    """
    Retrieve all notes.

    Response:
    {
        "notes": [
            {
                "id": 1,
                "title": "Note title",
                "content": "Note content"
            }
        ]
    }
    """
    return jsonify({"notes": notes}), 200

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note_by_id(note_id):
    """
    Retrieve a specific note by ID.

    URL parameter:
    - note_id: The ID of the note to retrieve.

    Response:
    - 200: If the note is found.
    - 404: If the note is not found.
    """
    for note in notes:
        if note["id"] == note_id:
            return jsonify(note), 200
    return jsonify({"message": "Note not found"}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)
