from app.task import Task
from app.comment import Comment 
from interfaces.filter_interface import Filter


class WhitespaceFilter(Filter):
    
    def is_filter(self, object) -> Task|Comment:
        if type(object) == Task: 
            object.title = object.title.strip()
            while object.title.count('  '):
                object.title = object.title.replace('  ', ' ')
            object.description = object.description.strip()
            while object.description.count('  '):
                object.description = object.description.replace('  ', ' ')
        else:
            object.message =  object.message.strip()
            while object.message.count('  '):
                object.message = object.message.replace('  ', ' ')                        
        return object