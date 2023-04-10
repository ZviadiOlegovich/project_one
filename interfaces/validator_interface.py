from abc import ABC, abstractmethod
from entities.task import Task

class Validator(ABC):# validator
    
    @abstractmethod
    def is_valid(self, task : Task) -> tuple[bool, str]:
        pass #isvalid
        