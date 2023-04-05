from app.task import Task
from app.comment import Comment 
from interfaces.filter_interface import Filter


class CapitalizeFilter(Filter):
    
    def is_filter(self, object) -> Task|Comment:
        if type(object) == Task:
            object.title = object.title.capitalize()
            object.description = object.description.capitalize()   
        else:
            object.message = object.message.capitalize()     
        return object