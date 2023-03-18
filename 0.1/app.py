from flask import Flask, jsonify, request
from db import connect_to_db, get_all_tasks, get_task_by_id, add_task, update_task, delete_task_by_id


app = Flask(__name__)

# Подключение к базе данных
db = connect_to_db("c:/Users/zoshc/workspace/project_one/mysql_config.json")


# Маршрут для главной страницы
@app.route('/') 
def index():
    return "This website is very bad."


# Маршрут для выполнения запроса GET
@app.route('/data/', methods=['GET'])
def get_all_tasks_handler():
    tasks = get_all_tasks(db)
    return jsonify(tasks)    


# Маршрут для выполнения запроса GET
@app.route('/data/<int:id>', methods=['GET'])
def get_task_by_id_handler(id):
    task = get_task_by_id(db, id)
    return jsonify(task)    


# Маршрут для выполнения запроса POST
@app.route('/data', methods=['POST'])
def add_task_handler():
    title = request.json.get('title')
    description = request.json.get('description')
    task_id = add_task(db, title, description)
    return jsonify({"Data added": 'successfully','TaskID': task_id})


# Маршрут для выполнения запроса PUT
@app.route('/data/<int:id>', methods=['PUT'])
def update_task_handler(id):
    status = request.form.get('status')
    result = update_task(db, id, status)
    if result:
        return f'Task {id}, status changed to {status}'
    else:
        return f'Task {id} not found'
    

# Маршрут для выполнения запроса DELETE    
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_task_handler(id):
    delete_task_by_id(db, id)
    return jsonify({"Data deleted": 'successfully', 'TaskID': id})


if __name__ == '__main__':
    app.run(debug=False, port=8000)