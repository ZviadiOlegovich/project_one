from db.mysql import Database
from validators.title_length import TitleLengthValidator
from validators.description_length import DescriptionLengthValidator
from validators.composite import Composite
from app.app import App
from flask import Flask
from routers.router import TaskRoutes

# Подключение к базе данных
db = Database("c:/Users/zoshc/workspace/mysql_config.json")
validator1  = TitleLengthValidator()
validator2  = DescriptionLengthValidator()
validator = Composite([validator1, validator2])
app = App(db, validator)
router = Flask(__name__)
task_routes = TaskRoutes(app, router)



if __name__ == '__main__':
    router.run(debug=False, port=8000)
