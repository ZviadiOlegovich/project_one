from interfaces.notify_interface import Notificator
from entities.event import Event
from interfaces.event_log_interface import EventLogStorage


class NotifyInLog(Notificator):
    def __init__(self, db : EventLogStorage):
        self.db = db
        
    def notify(self, event: Event):
        self.db.insert(event)
        return
    
