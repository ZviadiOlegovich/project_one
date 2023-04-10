class Comment:
    def __init__(self, id, task_id, author, message,
                  d_time=None):
        self.id = id
        self.task_id = task_id
        self.author = author 
        self.message = message
        self.d_time = d_time
        
        
    # def conver_to_json(lst: list) ->dict:
    #     return {'id': lst[0],'task_id': lst[1],
    #             'message': lst[2], 'd_time': lst[3]}
        
        
  
    def to_json(self):
        return ((f"id: {self.id}"),(f"task_id: {self.task_id}"), 
                (f"author: {self.author}"), (f"message: {self.message}"), 
                (f"d_time: {self.d_time}"))