
"""
Example script showing how to represent todo lists and todo entries in Python
data structures and how to implement endpoint for a REST API with Flask.

Requirements:
* flask
"""

import uuid

from flask import Flask, request, jsonify, abort


# initialize Flask server
app = Flask(__name__)

# create unique id for lists, entries
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
todo_1_id = uuid.uuid4()
todo_2_id = uuid.uuid4()
todo_3_id = uuid.uuid4()
todo_4_id = uuid.uuid4()

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
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# endpoint for creating a new todo list
@app.route('/todo-list', methods=['POST'])
def add_new_list():
    pass

# endpoint for getting all entries of a list (GET),
# deleting a complete list with all its entries (DELETE)
# and adding a new entry to an existing list (POST)
@app.route('/todo-list/<list_id>', methods=['GET', 'DELETE', 'POST'])
def handle_list(list_id):
    pass

# endpoint for updating an existing entry (PATCH)
# and deleting a single entry (DELETE)
@app.route('/entry/<entry_id>', methods=['PATCH', 'DELETE'])
def handle_entry(entry_id):
    pass

if __name__ == '__main__':
    # start Flask server
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
