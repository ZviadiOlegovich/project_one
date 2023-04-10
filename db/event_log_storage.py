# import mysql.connector
from interfaces.event_log_interface import EventLogStorage
from entities.event import Event
from datetime import datetime

class EventLogDb(EventLogStorage):
    def __init__(self, connect):
        self.db = connect
        
    def get_task_event_by_id(self, id: int) -> list:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM event_log WHERE task_id = %s", (id,))
        ans = cursor.fetchall()
        event =[Event(*e) for e in ans]
        self.db.commit() 
        cursor.close()               
        return event 
        
    def insert(self, event: Event): # notify
        cursor = self.db.cursor()
        date = datetime.now()
        cursor.execute("INSERT INTO event_log (task_id, assignee, event, date) VALUES (%s, %s, %s, %s)", 
                       (event.task_id, event.assignee ,event.event , date))
        self.db.commit()        
        cursor.close()
        return 