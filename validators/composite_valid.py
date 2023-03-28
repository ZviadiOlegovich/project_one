from app.task import Task
from app.validator_interface import Validator


class Composite(Validator):# title langth validator
    
    def __init__(self, validators : list):
        self.validators = validators
        
               
    def is_valid(self, task: Task) -> tuple[bool, str]:
        ok = True
        msg = ''
        for v in self.validators: 
            valid, err = v.is_valid(task)           
            if not valid:
                msg += err + "; "
                ok = False
        return ok , msg      
        