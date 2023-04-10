from abc import ABC, abstractmethod
from entities.task import Task
from entities.comment import Comment 

class Filter(ABC):# validator
    
    @abstractmethod
    def is_filter(self, args):
        pass #isvalid
        