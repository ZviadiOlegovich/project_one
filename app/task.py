class Task:
    def __init__(self, id, title, descrption, author_id, executor_id,
                 status='pending', start=None, end_time=None):
        self.id = id
        self.title = title
        self.description = descrption
        self.author_id = author_id
        self.executor_id = executor_id
        self.status = status
        self.start = start
        self.end_time = end_time      

  
    def to_json(self):
        # return {'id': self.id,'title': self.title, 'description': self.description,
                # 'author_id': self.author_id, 'executor_id': self.executor_id,
                # 'status': self.status, 'start': self.start, 'end_time': self.end_time}
                
        return ((f"id: {self.id}"),(f"title: {self.title}"), 
                (f"description: {self.description}"), 
                (f"author_id: {self.author_id}"), 
                (f"executor_id: {self.executor_id}"),
                (f"status: {self.status}"), (f"start: {self.start}"), 
                (f"end_time: {self.end_time}"))