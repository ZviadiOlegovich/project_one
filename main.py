from db.mysql import Database
# from app.task import Task
from app.app import App
from flask import Flask
from routers.router import TaskRoutes

# Подключение к базе данных
db = Database("c:/Users/zoshc/workspace/mysql_config.json")
app = App(db)
router = Flask(__name__)
task_routes = TaskRoutes(app, router)



if __name__ == '__main__':
    router.run(debug=False, port=8000)
