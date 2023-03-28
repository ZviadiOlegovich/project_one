from app.task import Task
from app.filter_interface import Filter


class WhitespaceFilter(Filter):
    
    def is_filter(self, task : Task) -> Task:
        task.title = task.title.strip()
        task.description = task.description.strip()        
        return task