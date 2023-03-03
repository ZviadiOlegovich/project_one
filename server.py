# Должны быть запущены 2 Docker конейнера: "MySQL" and "PHPadmin"(для подключения к БД)
from flask import Flask, request
import json
import mysql.connector

app = Flask(__name__)

def connect_to_db(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)

    db = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database'],
        port=config['port']
    )

    return db



# Подключение к базе данных
db = connect_to_db("mysql_config.json")


# Маршрут для главной страницы
@app.route('/') 
def index():
    return "This website is very bad."


# Маршрут для выполнения запроса GET
@app.route('/data/', methods=['GET'])
def get_task():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task")
    result = cursor.fetchall()
    db.commit() 
    cursor.close()
    return result    


# Маршрут для выполнения запроса GET
@app.route('/data/<int:id>', methods=['GET'])
def get_task_byid(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task WHERE id = %s", (id,))
    result = cursor.fetchall()
    db.commit() 
    cursor.close()
    return result    


# Маршрут для выполнения запроса POST
@app.route('/data', methods=['POST'])
def post_data():
    cursor = db.cursor()
    title = request.json.get('title')
    description = request.json.get('description')
    cursor.execute("INSERT INTO task (title, description) VALUES (%s, %s)", (title, description))
    db.commit()
    cursor.close()
    return 'Data added successfully' 


# Маршрут для выполнения запроса PUT
@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    cursor = db.cursor()
    status = request.form.get('status')
    cursor.execute("UPDATE task SET status=%s WHERE id=%s", (status, id))
    db.commit()
    cursor.close()
    return f'Task {id}, status changed to {status}'


# Маршрут для выполнения запроса DELETE
@app.route('/data/<int:id>', methods=['DELETE'])
def del_task_byid(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM task WHERE  id=%s", (id,))
    result = cursor.fetchall()
    db.commit() 
    cursor.close()
    return f'Task {id}, deleted from DB'  


if __name__ == '__main__':
    app.run(debug=False, port=8000)


