from app.task import Task
from app.comment import Comment
from app.comment_interface import CommentStorage
from app.storage import Storage
from app.validator_interface import Validator
from app.filter_interface import Filter
from app.add_eventL_interface import Notificator
# from app.notify_interface import EventLogStorage
 

class App:
    def __init__(self, db: Storage, validator : Validator,
                 filter : Filter, notify: Notificator,
                 comment: CommentStorage):
        self.db = db
        self.vd = validator
        self.fl = filter
        self.nf = notify
        self.cm = comment
        
        
    def get_comments_by_id(self, id):               
        comments = self.cm.get_comment(id)
        return comments
    
    def insert_comment(self, comment: Comment):
        comment = self.cm.add_comment(comment)        
        return {"Commetn added": 'successfully', 'Comment_id': comment.id}
        

    def info(self):
        return self.db.info()  
    
    def find_tasks(self):
        return self.db.get_all_tasks()
    
    def sort_by_status(self, status):
        return self.db.get_sorted_task(status)
    
    def find_task_by_id(self, id) -> Task:               
        task = self.db.get_task_by_id(id)
        return task
        


    def create_new_task(self, task: Task):
        task = self.fl.is_filter(task)
        ok, err = self.vd.is_valid(task)
        if ok:
            task = self.db.insert_task(task)
            event = 'created'
            self.nf.notify(task, event)
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
                event = 'updated'
                self.nf.notify(task, event)
                return f'Task {task.id}, status changed to {task.status}'
            else:
                return err
        else:
            return f"task {task.id} - not found"
        
    def delete_task_by_id(self, id):
        task = self.db.get_task_by_id(id)
        if task != []:            
            event = 'deleted'            
            self.nf.notify(task, event)
            self.db.delete_task_by_id(id)
            return f'Task {id}, deleted from DB'
        else:
            return f"task {id} - not found"
        
    

    