from entities.task import Task
from entities.comment import Comment 
from entities.user import User
import re
from interfaces.filter_interface import Filter


class WhitespaceFilter(Filter):
    
    def is_filter(self, args) :
        args = [s.strip() for s in args]
        return [re.sub(' +', ' ', s) for s in args]
    
    # def is_filter(self, object) -> Task|Comment|User:
    #     if type(object) == Task: 
    #         object.title = object.title.strip()
    #         while object.title.count('  '):
    #             object.title = object.title.replace('  ', ' ')
    #         object.description = object.description.strip()
    #         while object.description.count('  '):
    #             object.description = object.description.replace('  ', ' ')
    #     elif type(object) == Comment:
    #         object.message =  object.message.strip()
    #         while object.message.count('  '):
    #             object.message = object.message.replace('  ', ' ')      
    #     else:
    #         object.name = object.name.strip()
    #         while object.name.count(' '):
    #             object.name = object.name.replace(' ', '')
    #         object.surname = object.surname.strip()
    #         while object.surname.count('  '):
    #             object.surname = object.surname.replace('  ', ' ')
                              
    #     return object