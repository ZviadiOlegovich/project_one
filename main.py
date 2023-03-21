from db.mysql import Database
from app.task import Task
from app.app import App
from flask import Flask, jsonify, request

# Подключение к базе данных
db = Database("c:/Users/zoshc/workspace/mysql_config.json")
app = App(db)
router = Flask(__name__)




@router.route('/') 
def index():
    return app.info()


# Маршрут для выполнения запроса GET
@router.route('/data/', methods=['GET'])
def get_all_tasks_handler():
    tasks = app.find_tasks()
    return jsonify(tasks)    


# Маршрут для выполнения запроса GET
@router.route('/data/<int:id>', methods=['GET'])
def get_task_by_id_handler(id):
    task = app.find_task_by_id(id)
    return jsonify(task)    


# Маршрут для выполнения запроса POST
@router.route('/data', methods=['POST'])
def insert_task_handler():    
    title = request.json.get('title')
    description = request.json.get('description')
    task = Task(0,title, description)
    result = app.create_task(task)
    # task = Task( task_id, title, description)
    return jsonify(result)


# Маршрут для выполнения запроса PUT
@router.route('/data/<int:id>', methods=['PUT'])
def update_task_handler(id):
    title = request.json.get('title')
    description = request.json.get('description')
    status = request.json.get('status')
    task = Task(id, title, description, status)    
    result = app.update_task(task)
    return jsonify(result)


# Маршрут для выполнения запроса DELETE
@router.route('/data/<int:id>', methods=['DELETE'])
def delete_task_handler(id):
    result = app.delete_task_by_id(id)
    return jsonify({'result': result})

if __name__ == '__main__':
    router.run(debug=False, port=8000)