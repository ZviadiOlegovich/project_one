class User:
    def __init__(self, id, name, surname, position):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        
        
    def to_json(self):
        return ((f"id: {self.id}"),(f"name: {self.name}"), 
                (f"surname: {self.surname}"), (f"position: {self.position}"))