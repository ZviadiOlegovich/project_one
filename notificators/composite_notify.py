from app.notify_interface import Notify
from app.task import Task

class CompositeNotify(Notify):
    
    def __init__(self, notifies : list):
        self.notifies = notifies
        
    def is_notify(self, task: Task, event: str, date):
        
        for n in self.notifies: 
            n.is_notify(task, event, date)   
             
        return