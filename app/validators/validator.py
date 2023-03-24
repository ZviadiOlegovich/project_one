from app.task import Task
from app.validator_interface import Validator

class TitleLangthValidator(Validator):# title langth validator
    # min = 5
    # max = 60
    
    def is_valid(self, task: Task) -> bool:
        if 5 <= len(task.title) < 60:
            return True
        else:
            return False
        