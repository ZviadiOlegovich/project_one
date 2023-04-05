from app.task import Task
from app.comment import Comment 
from interfaces.filter_interface import Filter


class CompositeFilter(Filter):# title langth validator
    
    def __init__(self, filters : list):
        self.filters = filters
        
               
    def is_filter(self, object) -> Task|Comment:
        
        for f in self.filters: 
            object = f.is_filter(object)           
            
        return  object