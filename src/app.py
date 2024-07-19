from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)

todos = [
    {"label": "Sample Todo 1", "done": True},
    {"label": "Sample Todo 2", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json()  # Use get_json() to parse the JSON body
    print("Incoming request with the following body", request_body)
    todos.append(request_body)  # Add the new todo to the list
    return jsonify(todos)  # Return the updated list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Check if the position is valid
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Invalid position"}), 400
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True)