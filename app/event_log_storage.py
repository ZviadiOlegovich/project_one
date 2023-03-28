# import mysql.connector
from app.notify_interface import Notify
from app.task import Task

class EventLog(Notify):
    def __init__(self, connect):
        self.db = connect
        
    def is_notify(self, task: Task, event: str, date) -> Task:
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO event_log (task_id, event, date) VALUES (%s, %s, %s)", 
                       (task.id, event, date))
        self.db.commit()        
        cursor.close()
        return 