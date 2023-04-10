from abc import ABC, abstractmethod
from entities.event import Event

class EventLogStorage(ABC):
    
    @abstractmethod
    def insert(self, event : Event): 
        pass
    
    @abstractmethod
    def get_task_event_by_id(self, id : int):
        pass