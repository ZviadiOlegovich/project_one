from abc import ABC, abstractmethod
from app.task import Task

class ValidIn(ABC):
    
    @abstractmethod
    def valid_title(self, task : Task) -> bool:
        pass
        