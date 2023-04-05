from app.task import Task
from app.comment import Comment
from app.user import User
from interfaces.user_st_interface import UserStorage
from interfaces.comment_interface import CommentStorage
from interfaces.mysql_interface import Storage
from interfaces.validator_interface import Validator
from interfaces.filter_interface import Filter
from interfaces.event_log_interface import Notificator
 

class App:
    def __init__(self, db: Storage, validator : Validator,
                 filter : Filter, notify: Notificator,
                 comment: CommentStorage, user: UserStorage):
        self.db = db
        self.vd = validator
        self.fl = filter
        self.nf = notify
        self.cm = comment
        self.us = user
        
        
    def get_user_by_id(self, id) -> User:               
        user = self.us.get_user_by_id(id)
        return user
    
    
    def insert_user(self, user: User):        
        user = self.us.insert_user(user)        
        return {"User added": 'successfully', 'User_id': user.id}
    
    
    def delete_user_by_id(self, id):
        user = self.us.get_user_by_id(id)
        if type(user) == User:            
            # event = 'deleted'            
            # self.nf.notify(task, event)
            self.us.delete_user_by_id(id)
            return f'User {id}, deleted from DB'
        else:
            return f"User {id} - not found"
        
        
        
    def get_comments_by_id(self, id) -> list:               
        comments = self.us.get_comments_by_id(id)
        return comments
    
    
    def insert_comment(self, comment: Comment):
        comment = self.fl.is_filter(comment)
        comment = self.cm.add_comment(comment)        
        return {"Comment added": 'successfully', 'Comment_id': comment.id}
 
 
    def sort_by_status(self, status):
        return self.db.get_sorted_task(status)
           

    def info(self):
        return self.db.info()  
    
    
    def get_all_tasks(self):
        return self.db.get_all_tasks()
    
    
    def get_task_by_id(self, id):               
        task = self.db.get_task_by_id(id)        
        return task
        

    def insert_task(self, task: Task):
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
        
    

    