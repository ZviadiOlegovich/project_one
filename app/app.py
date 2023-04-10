from entities.task import Task
from entities.comment import Comment
from entities.user import User
from entities.event import Event
from interfaces.user_st_interface import UserStorage
from interfaces.comment_interface import CommentStorage
from interfaces.mysql_interface import Storage
from interfaces.validator_interface import Validator
from interfaces.filter_interface import Filter
from interfaces.notify_interface import Notificator
from interfaces.event_log_interface import EventLogStorage 

class App:
    def __init__(self, db: Storage, comment: CommentStorage, user: UserStorage,
                 els: EventLogStorage, validator : Validator,
                 filter : Filter, notify: Notificator,):
        self.db = db       
        self.cm = comment
        self.us = user
        self.els = els 
        self.vd = validator
        self.fl = filter
        self.nf = notify
    
    
    # EVENT LOG    
    def get_task_event_by_id(self, id) -> list:               
        events = self.els.get_task_event_by_id(id)
        return events
    
        
    # USER    
    def get_user_by_id(self, id) -> User:               
        user = self.us.get_user_by_id(id)
        return user
    
    
    def insert_user(self, user: User): 
        user.name, user.surname = self.fl.is_filter([user.name, user.surname])       
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
        
    # COMMENTS    
    def get_comments_by_id(self, id) -> list:               
        comments = self.cm.get_comments_by_id(id)
        return comments
    
    
    def insert_comment(self, comment: Comment):
        comment.message = self.fl.is_filter([comment.message])[0]
        comment = self.cm.add_comment(comment)        
        return {"Comment added": 'successfully', 'Comment_id': comment.id}
 
    # TRASH
    def sort_by_status(self, status):
        return self.db.get_sorted_task(status)
           

    def info(self):
        return self.db.info()  
    
    # TASKS
    def get_all_tasks(self):
        return self.db.get_all_tasks()
    
    
    def get_task_by_id(self, id):               
        task = self.db.get_task_by_id(id)        
        return task
        

    def insert_task(self, task: Task):
        task.title, task.description = self.fl.is_filter([task.title, task.description])
        ok, err = self.vd.is_valid(task)
        if ok:
            task = self.db.insert_task(task)
            event = Event(0, task.id, task.author, 'created')
            self.nf.notify(event)
            return {"Data added": 'successfully', 'TaskID': task.id}
        else:
            return {"Data added": 'unsuccessfully', 
                    'Error': err}
    
    
    def update_task(self, task: Task):        
        task.title, task.description = self.fl.is_filter([task.title, task.description])
        rs = self.db.get_task_by_id(task.id)
        if rs != []:
            ok, err = self.vd.is_valid(task)
            if ok:
                self.db.update_task(task)
                event = Event(0, task.id, task.assignee, 'updated')
                self.nf.notify(event)
                return f'Task {task.id}, status changed to {task.status}'
            else:
                return err
        else:
            return f"task {task.id} - not found"
        
        
    def delete_task_by_id(self, id):
        task = self.db.get_task_by_id(id)
        if task != []:            
            event = Event(0, task.id, task.assignee, 'deleted')        
            self.db.delete_task_by_id(id)           
            self.nf.notify(event)            
            return f'Task {id}, deleted from DB'
        else:
            return f"task {id} - not found"
        
    

    