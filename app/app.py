from app.task import Task
from app.storage import Storage

class App:
    def __init__(self, db: Storage):
        self.db = db

    def info(self):
        return self.db.info()  
    
    def find_tasks(self):
        return self.db.get_all_tasks()
    
    def find_task_by_id(self, id):
        return self.db.get_task_by_id(id)

    def create_task(self, task: Task):
        rs = self.db.insert_task(task)
        return {"Data added": 'successfully', 'TaskID': rs} 
    
    def update_task(self, task: Task):
        self.db.update_task(task)
        return f'Task {task.id}, status changed to {task.status}'
    
    def delete_task_by_id(self, id):
        self.db.delete_task_by_id(id)
        return f'Task {id}, deleted from DB'
    

    