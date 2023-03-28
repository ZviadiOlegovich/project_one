from abc import ABC, abstractmethod
from app.task import Task

class Notify(ABC):
    
    @abstractmethod
    def is_notify(self, task : Task, event : str, date): 
        pass