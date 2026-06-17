
"""
Example script showing how to represent todo lists and todo entries in Python
data structures and how to implement endpoint for a REST API with Flask.

Requirements:
* flask
"""

import uuid

from flask import Flask, request, jsonify


# initialize Flask server
app = Flask(__name__)

# create unique id for lists, entries
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
todo_1_id = str(uuid.uuid4())
todo_2_id = str(uuid.uuid4())
todo_3_id = str(uuid.uuid4())
todo_4_id = str(uuid.uuid4())

# define internal data structures with example data
todo_lists = [
    {'id': todo_list_1_id, 'name': 'Einkaufsliste'},
    {'id': todo_list_2_id, 'name': 'Arbeitsliste'},
    {'id': todo_list_3_id, 'name': 'Wunschliste'}
]
todos = [
    {'id': todo_1_id, 'name': 'Milch', 'description': 'Meine Einkäufe für diese Woche', 'list_id': todo_list_1_id},
    {'id': todo_2_id, 'name': 'Computer', 'description': 'Computer kaufen', 'list_id': todo_list_2_id},
    {'id': todo_3_id, 'name': 'Geschenk', 'description': 'PS5 Controller', 'list_id': todo_list_3_id},
    {'id': todo_4_id, 'name': 'Eier', 'description': 'Meine Einkäufe für diese Woche', 'list_id': todo_list_1_id}
]

# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE, PATCH'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Startseite – gibt alle Listen zurück
@app.route('/', methods=['GET'])
def index():
    return jsonify(todo_lists), 200

# endpoint for creating a new todo list
@app.route('/todo-list', methods=['POST'])
def add_new_list():
    try:
        data = request.json
        if not data or 'name' not in data:
            return jsonify({"message": "Invalid request"}), 406
        new_list = {
            'id': str(uuid.uuid4()),
            'name': data['name']
        }
        todo_lists.append(new_list)
        return jsonify(new_list), 201
    except Exception:
        return jsonify({"message": "Server error"}), 500


# endpoint for getting all entries of a list (GET),
# deleting a complete list with all its entries (DELETE)
# and adding a new entry to an existing list (POST)
@app.route('/todo-list/<list_id>', methods=['GET', 'DELETE', 'POST'])
def handle_list(list_id):
    if request.method == 'GET':
        found = False
        for current_list in todo_lists:
            if current_list['id'] == list_id:
                found = True
                break
        if not found:
            return jsonify({"message": "Invalid list ID"}), 404

        try:
            entries = []
            for todo in todos:
                if todo['list_id'] == list_id:
                    entries.append(todo)
            return jsonify(entries), 200
        except Exception:
            return jsonify({"message": "Server error"}), 500

    elif request.method == 'DELETE':
        found = False
        for current_list in todo_lists:
            if current_list['id'] == list_id:
                found = True
                list_to_delete = current_list
                break
        if not found:
            return jsonify({"message": "Invalid list ID"}), 404

        try:
            todo_lists.remove(list_to_delete)
            keep_list = []
            for entry in todos:
                if entry['list_id'] != list_id:
                    keep_list.append(entry)
            todos[:] = keep_list
            return jsonify({"message": "List deleted"}), 204
        except Exception:
            return jsonify({"message": "Server error"}), 500

    elif request.method == 'POST':
        found = False
        for current_list in todo_lists:
            if current_list['id'] == list_id:
                found = True
                break
        if not found:
            return jsonify({"message": "Invalid list ID"}), 404

        try:
            data = request.json
            if not data or 'name' not in data:
                return jsonify({"message": "Invalid request data"}), 406

            new_entry = {
                'id': str(uuid.uuid4()),
                'name': data['name'],
                'description': data.get('description', ''),
                'list_id': list_id
            }
            todos.append(new_entry)
            return jsonify(new_entry), 201
        except Exception:
            return jsonify({"message": "Server error"}), 500

# endpoint for updating an existing entry (PATCH)
# and deleting a single entry (DELETE)
@app.route('/entry/<entry_id>', methods=['PATCH', 'DELETE'])
def handle_entry(entry_id):
    if request.method == 'PATCH':
        found = False
        entry_to_update = None
        for entry in todos:
            if entry['id'] == entry_id:
                found = True
                entry_to_update = entry
                break
        if not found:
            return jsonify({"message": "Invalid entry ID"}), 404

        try:
            data = request.json
            if not data:
                return jsonify({"message": "Invalid request data"}), 406

            if 'name' in data:
                entry_to_update['name'] = data['name']
            if 'description' in data:
                entry_to_update['description'] = data['description']

            return jsonify(entry_to_update), 200
        except Exception:
            return jsonify({"message": "Server error"}), 500

    elif request.method == 'DELETE':
        found = False
        entry_to_delete = None
        for entry in todos:
            if entry['id'] == entry_id:
                found = True
                entry_to_delete = entry
                break
        if not found:
            return jsonify({"message": "Invalid entry ID"}), 404

        try:
            todos.remove(entry_to_delete)
            return jsonify({"message": "Entry deleted"}), 204
        except Exception:
            return jsonify({"message": "Server error"}), 500

if __name__ == '__main__':
    # start Flask server
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
