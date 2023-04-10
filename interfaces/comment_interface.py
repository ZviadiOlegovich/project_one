from abc import ABC, abstractmethod
from entities.comment import Comment

class CommentStorage(ABC):
    
        
    @abstractmethod
    def get_comments_by_id(self, id : int) -> list:
        pass
    
    
    @abstractmethod
    def add_comment(self, comment: Comment): 
        pass