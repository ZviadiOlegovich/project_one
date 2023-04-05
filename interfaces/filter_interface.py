from abc import ABC, abstractmethod
from app.task import Task
from app.comment import Comment 

class Filter(ABC):# validator
    
    @abstractmethod
    def is_filter(self, object) -> Task|Comment:
        pass #isvalid
        