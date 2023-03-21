from abc import ABC, abstractmethod
from app.task import Task

class Storage(ABC):
 
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def get_all_tasks(self, id: int) -> Task:
        pass

    @abstractmethod
    def get_task_by_id(self, id: int) -> Task:
        pass

    @abstractmethod
    def insert_task(self, task: Task) -> Task:
        pass

    @abstractmethod
    def update_task(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete_task_by_id(self, id: int):
        pass

   
