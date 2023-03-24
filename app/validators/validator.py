from app.task import Task
from app.validator_interface import ValidIn

class IsValid(ValidIn):
    # min = 5
    # max = 60
    
    def valid_title(self, task: Task) -> bool:
        if 5 <= len(task.title) < 60:
            return True
        else:
            return False
        