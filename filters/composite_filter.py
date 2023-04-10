from entities.task import Task
from entities.comment import Comment 
from interfaces.filter_interface import Filter
from entities.user import User


class CompositeFilter(Filter):# title langth validator
    
    def __init__(self, filters : list):
        self.filters = filters
        
               
    def is_filter(self, args) -> list:
        
        for f in self.filters: 
            args = f.is_filter(args)           
            
        return  args