from abc import ABC, abstractmethod
from entities.user import User

class UserStorage(ABC):
    
        
    @abstractmethod
    def get_user_by_id(self, id : int) -> User:
        pass
    
    
    @abstractmethod
    def insert_user(self, user: User): 
        pass
    
    
    @abstractmethod
    def delete_user_by_id(self, id : int) -> User:
        pass