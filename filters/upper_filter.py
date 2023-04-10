from entities.task import Task
from entities.comment import Comment 
from entities.user import User
from interfaces.filter_interface import Filter


class CapitalizeFilter(Filter):
    
    def is_filter(self, args) -> list:
        return [s.capitalize() for s in args]
    
    
    # def is_filter(self, object) -> Task|Comment|User:
    #     if type(object) == Task:
    #         object.title = object.title.capitalize()
    #         object.description = object.description.capitalize()   
    #     elif type(object) == Comment:
    #         object.message = object.message.capitalize()
    #     else:
    #         object.name = object.name.capitalize()
    #         object.surname = object.surname.capitalize() 
                 
    #     return object