
class Task:
    def __init__(self, id, title, descrption, status ='pending'):
        self.id = id
        self.title = title
        self.description = descrption
        self.status = status