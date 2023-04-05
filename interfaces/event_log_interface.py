from abc import ABC, abstractmethod
from app.task import Task

class Notificator(ABC):
    
    @abstractmethod
    def notify(self, task : Task, event : str): 
        pass