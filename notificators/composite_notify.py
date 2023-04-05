from interfaces.event_log_interface import Notificator
from app.task import Task

class CompositeNotify(Notificator):
    
    def __init__(self, notifies : list):
        self.notifies = notifies
        
    def notify(self, task: Task, event: str):
        
        for n in self.notifies: 
            n.notify(task, event)   
             
        return
    
