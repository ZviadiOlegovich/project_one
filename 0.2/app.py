from flask import Flask, jsonify, request
from db import DB


app = Flask(__name__)

# Подключение к базе данных
db = DB("c:/Users/zoshc/workspace/project_one/mysql_config.json")


# Маршрут для главной страницы
@app.route('/') 
def index():
    return "This website is very bad."


# Маршрут для выполнения запроса GET
@app.route('/data/', methods=['GET'])
def get_all_tasks_handler():
    tasks = db.get_all_tasks()
    return jsonify(tasks)    


# Маршрут для выполнения запроса GET
@app.route('/data/<int:id>', methods=['GET'])
def get_task_by_id_handler(id):
    task = db.get_task_by_id(id)
    return jsonify(task)    


# Маршрут для выполнения запроса POST
@app.route('/data', methods=['POST'])
def add_task_handler():
    title = request.json.get('title')
    description = request.json.get('description')
    task_id = db.add_task(title, description)
    return jsonify({"Data added": 'successfully','TaskID': task_id})


# Маршрут для выполнения запроса PUT
@app.route('/data/<int:id>', methods=['PUT'])
def update_task_handler(id):
    status = request.form.get('status')
    result = db.update_task(id, status)
    return jsonify(result)


# Маршрут для выполнения запроса DELETE
@app.route('/data/<int:id>', methods=['DELETE'])
def delete_task_handler(id):
    result = db.delete_task_by_id(id)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=False, port=8000)