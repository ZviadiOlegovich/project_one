from app.task import Task
from app.storage import Storage
from app.validator_interface import Validator
 

class App:
    def __init__(self, db: Storage, validator : Validator):
        self.db = db
        self.vd = validator

    def info(self):
        return self.db.info()  
    
    def find_tasks(self):
        return self.db.get_all_tasks()
    
    def find_task_by_id(self, id):               
        task = self.db.get_task_by_id(id)
        return task
        


    def create_new_task(self, task: Task):
        ok, err = self.vd.is_valid(task)
        if ok:
            rs = self.db.insert_task(task)
            return {"Data added": 'successfully', 'TaskID': rs}
        else:
            return {"Data added": 'unsuccessfully', 
                    'Error': err}
    
    def update_task(self, task: Task):
        rs = self.db.get_task_by_id(task.id)
        if rs != []:
            ok, err = self.vd.is_valid(task)
            if ok:
                self.db.update_task(task)
                return f'Task {task.id}, status changed to {task.status}'
            else:
                return err
        else:
            return f"task {task.id} - not found"
        
    def delete_task_by_id(self, id):
        rs = self.db.get_task_by_id(id)
        if rs != []:
            self.db.delete_task_by_id(id)
            return f'Task {id}, deleted from DB'
        else:
            return f"task {id} - not found"
        
    

    