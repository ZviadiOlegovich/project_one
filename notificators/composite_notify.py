from interfaces.notify_interface import Notificator
from entities.event import Event


class CompositeNotify(Notificator):
    
    def __init__(self, notifies : list):
        self.notifies = notifies
        
    def notify(self, event: Event):
        
        for n in self.notifies: 
            n.notify(event)   
             
        return
    
