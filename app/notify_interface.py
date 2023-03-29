from abc import ABC, abstractmethod
from app.task import Task

class EventLogStorage(ABC):
    
    @abstractmethod
    def insert(self, task : Task, event : str): 
        pass
    
    @abstractmethod
    def task_event_by_id(self, id : int):
        pass