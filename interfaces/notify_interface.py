from abc import ABC, abstractmethod
from entities.event import Event

class Notificator(ABC):
    
    @abstractmethod
    def notify(self, event : Event): 
        pass