from app.add_eventL_interface import Notificator
from app.task import Task
from app.notify_interface import EventLogStorage

class EventLog(Notificator):
    def __init__(self, db : EventLogStorage):
        self.db = db
        
    def notify(self, task: Task, event: str):
        self.db.insert(task, event)
        return
    
