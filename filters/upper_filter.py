from app.task import Task
from app.filter_interface import Filter


class CapitalizeFilter(Filter):
    
    def is_filter(self, task : Task) -> Task:
        task.title = task.title.capitalize()
        task.description = task.description.capitalize()        
        return task