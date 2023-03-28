from abc import ABC, abstractmethod
from app.task import Task

class Filter(ABC):# validator
    
    @abstractmethod
    def is_filter(self, task : Task) -> Task:
        pass #isvalid
        