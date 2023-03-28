from app.task import Task
from app.filter_interface import Filter


class CompositeFilter(Filter):# title langth validator
    
    def __init__(self, filters : list):
        self.filters = filters
        
               
    def is_filter(self, task: Task) -> Task:
        
        for f in self.filters: 
            task = f.is_filter(task)           
            
        return  task