import json
import mysql.connector
from db.mysql_storage import MySQLDb
from db.event_log_storage import EventLogDb
from db.comment_storage import CommentDb
from db.user_storage import UserDb
from validators.title_length import TitleLengthValidator
from validators.description_length import DescriptionLengthValidator
from validators.composite_valid import Composite
from filters.trip_filter import WhitespaceFilter
from filters.upper_filter import CapitalizeFilter
from filters.composite_filter import CompositeFilter
from notificators.notify_in_log import NotifyInLog
from notificators.composite_notify import CompositeNotify
from app.app import App
from flask import Flask
from routers.router import TaskRoutes

# Подключение к базе данных
with open("c:/Users/zoshc/workspace/mysql_config.json", 'r') as f:
    config = json.load(f)

db_con = mysql.connector.connect(host=config['host'],
                                 user=config['user'],
                                 password=config['password'],
                                 database=config['database'],
                                 port=config['port'])


db = MySQLDb(db_con)
els = EventLogDb(db_con)
cmnt = CommentDb(db_con) 
user = UserDb(db_con)
notify1 = NotifyInLog(els)
notify = CompositeNotify([notify1])
validator1, validator2  = TitleLengthValidator(), DescriptionLengthValidator()
validator = Composite([validator1, validator2])
filter1, filter2 = WhitespaceFilter(), CapitalizeFilter()
filter = CompositeFilter([filter1, filter2])
app = App(db, cmnt, user, els, validator, filter, notify)
router = Flask(__name__)
task_routes = TaskRoutes(app, router)



if __name__ == '__main__':
    router.run(debug=False, port=8000)
