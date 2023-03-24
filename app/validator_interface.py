from abc import ABC, abstractmethod
from app.task import Task

class Validator(ABC):# validator
    
    @abstractmethod
    def is_valid(self, task : Task) -> bool:
        pass #isvalid
        