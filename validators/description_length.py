from app.task import Task
from interfaces.validator_interface import Validator

class DescriptionLengthValidator(Validator):# title langth validator
        
    def is_valid(self, task: Task) -> tuple[bool, str]:
        if 20 <= len(task.description) < 200:
            return True, ''
        else:
            return False, 'Description lenght wrong'
        