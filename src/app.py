from flask import Flask, jsonify, request

todos = [
         {"label": "Primera tarea", "done": True},
         {"label": "Segunda tarea", "done": False}
         ]

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return '<h1>Hello World</h1>'

@app.route('/tasks', methods=['GET'])
def task_list():
    data_to_json = jsonify(todos)
    return data_to_json

@app.route('/tasks', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Request with body: ", request_body)
    todos.append(request_body)
    return 'Respuesta POST'

@app.route('/tasks/<int:position>', methods=['DELETE'])
def delete_task(position):
    print(f'El elemento número {position} será borrado.')
    if position > len(todos):
        print(f'El elemento {position} no existe en la lista.')
        return 'El elemento no existe en la lista.'
    deleted_task = todos[position-1]
    del todos[position-1]
    return f'Se ha borrado el registro: {deleted_task}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)