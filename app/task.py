
class Task:
    def __init__(self, id, title, descrption,
                 status='pending', start=None, end_time=None):
        self.id = id
        self.title = title
        self.description = descrption
        self.status = status
        self.start = start
        self.end_time = end_time
        

    def conver_to_json(lst: list) ->dict:
        return {'id': lst[0],'title': lst[1],
                'description': lst[2], 'status': lst[3],
                'start': lst[4], 'end_time': lst[5]}
        
    def to_json(self):
        return {'id': self.id,'title': self.title,
                'description': self.description, 'status': self.status,
                'start': self.start, 'end_time': self.end_time}