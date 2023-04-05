# import mysql.connector
from interfaces.notify_interface import EventLogStorage
from app.task import Task
from datetime import datetime

class EventLogDb(EventLogStorage):
    def __init__(self, connect):
        self.db = connect
        
    def task_event_by_id(self, id: int):
        pass
        
    def insert(self, task: Task, event: str) -> Task: # notify
        cursor = self.db.cursor()
        date = datetime.now()
        cursor.execute("INSERT INTO event_log (task_id, user_id, event, date) VALUES (%s, %s, %s, %s)", 
                       (task.id, task.author_id if event == 'created' else task.executor_id ,event, date))
        self.db.commit()        
        cursor.close()
        return 