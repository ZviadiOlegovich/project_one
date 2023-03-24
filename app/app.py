from app.task import Task
from app.storage import Storage
from app.validator_interface import ValidIn
 

class App:
    def __init__(self, db: Storage, validator : ValidIn):
        self.db = db
        self.vd = validator

    def info(self):
        return self.db.info()  
    
    def find_tasks(self):
        return self.db.get_all_tasks()
    
    def find_task_by_id(self, id):
        id1 = id        
        ts = self.db.get_task_by_id(id)
        if ts.id > 0:
            return ts
        else:
            return f"task {id1} - not found1"


    def create_new_task(self, task: Task):
        if self.vd.valid_title(task):
            rs = self.db.insert_task(task)
            return {"Data added": 'successfully', 'TaskID': rs}
        else:
            return {"Data added": 'unsuccessfully', 
                    'Error': "Task title must between 5 on 60 simbols"}
    
    def update_task(self, task: Task):
        rs = self.db.get_task_by_id(task.id)
        if rs != []:
            if self.vd.valid_title(task):
                self.db.update_task(task)
                return f'Task {task.id}, status changed to {task.status}'
            else:
                return "Task title must between 5 on 60 simbols"
        else:
            return f"task {task.id} - not found"
        
    def delete_task_by_id(self, id):
        rs = self.db.get_task_by_id(id)
        if rs != []:
            self.db.delete_task_by_id(id)
            return f'Task {id}, deleted from DB'
        else:
            return f"task {id} - not found"
        
    

    