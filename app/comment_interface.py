from abc import ABC, abstractmethod
from app.comment import Comment

class CommentStorage(ABC):
    
        
    @abstractmethod
    def get_comment(self, id : int) -> list:
        pass
    
    
    @abstractmethod
    def add_comment(self, comment: Comment): 
        pass