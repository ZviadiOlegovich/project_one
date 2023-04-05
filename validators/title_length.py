from app.task import Task
from interfaces.validator_interface import Validator

class TitleLengthValidator(Validator):# title langth validator
    
    def is_valid(self, task: Task) -> tuple[bool, str]:
        if 5 <= len(task.title) < 60:
            return True, ''
        else:
            return False, 'Title lenght wrong'
        