# import mysql.connector
from app.notify_interface import EventLogStorage
from app.task import Task
from datetime import datetime

class EventLOGdb(EventLogStorage):
    def __init__(self, connect):
        self.db = connect
        
    def task_event_by_id(self, id: int):
        pass
        
    def insert(self, task: Task, event: str) -> Task: # notify
        cursor = self.db.cursor()
        date = datetime.now()
        cursor.execute("INSERT INTO event_log (task_id, event, date) VALUES (%s, %s, %s)", 
                       (task.id, event, date))
        self.db.commit()        
        cursor.close()
        return 