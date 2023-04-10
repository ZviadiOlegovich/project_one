class Event:
    def __init__(self, id, task_id, assignee, event,
                  d_time=None):
        self.id = id
        self.task_id = task_id
        self.assignee = assignee  # author
        self.event = event
        self.d_time = d_time    
                     
  
    def to_json(self):
        return ((f"id: {self.id}"),(f"task_id: {self.task_id}"), 
                (f"assignee: {self.assignee}"), (f"event: {self.event}"), 
                (f"d_time: {self.d_time}"))