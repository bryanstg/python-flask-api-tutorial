from flask import Flask, jsonify, request
import json
print(__name__)
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    #Cambias el request a diccionario python.
    to_dict = json.loads(request_body)
    todos.append(to_dict)
    print(todos)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)

    print("This is the position to delete: ",position)
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='192.168.0.5', port=3245, debug=True)