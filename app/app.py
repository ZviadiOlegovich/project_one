from app.task import Task
from app.storage import Storage
from app.validator_interface import Validator
from app.filter_interface import Filter
from app.notify_interface import Notify
from datetime import datetime
 

class App:
    def __init__(self, db: Storage, validator : Validator,
                 filter : Filter, notify: Notify):
        self.db = db
        self.vd = validator
        self.fl = filter
        self.nf = notify

    def info(self):
        return self.db.info()  
    
    def find_tasks(self):
        return self.db.get_all_tasks()
    
    def find_task_by_id(self, id):               
        task = self.db.get_task_by_id(id)
        return task
        


    def create_new_task(self, task: Task):
        task = self.fl.is_filter(task)
        ok, err = self.vd.is_valid(task)
        if ok:
            task = self.db.insert_task(task)
            event, date = 'created', datetime.now()
            self.nf.is_notify(task, event, date)
            return {"Data added": 'successfully', 'TaskID': task.id}
        else:
            return {"Data added": 'unsuccessfully', 
                    'Error': err}
    
    def update_task(self, task: Task):        
        task = self.fl.is_filter(task)
        rs = self.db.get_task_by_id(task.id)
        if rs != []:
            ok, err = self.vd.is_valid(task)
            if ok:
                self.db.update_task(task)
                event, date = 'updated', datetime.now()
                self.nf.is_notify(task, event, date)
                return f'Task {task.id}, status changed to {task.status}'
            else:
                return err
        else:
            return f"task {task.id} - not found"
        
    def delete_task_by_id(self, id):
        task = self.db.get_task_by_id(id)
        if task != []:            
            event, date = 'deleted', datetime.now()            
            self.nf.is_notify(task, event, date)
            self.db.delete_task_by_id(id)
            return f'Task {id}, deleted from DB'
        else:
            return f"task {id} - not found"
        
    

    