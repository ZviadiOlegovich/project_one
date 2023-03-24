from db.mysql import Database
from app.validators.validator import TitleLangthValidator
from app.app import App
from flask import Flask
from routers.router import TaskRoutes

# Подключение к базе данных
db = Database("c:/Users/zoshc/workspace/mysql_config.json")
validator = TitleLangthValidator()
app = App(db, validator)
router = Flask(__name__)
task_routes = TaskRoutes(app, router)



if __name__ == '__main__':
    router.run(debug=False, port=8000)
