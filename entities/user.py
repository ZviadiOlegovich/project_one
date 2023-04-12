from collections import OrderedDict


class User:
    def __init__(self, id, name, surname, position):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position # директр менеджер юзер
        
        
    def to_dict(self):
        # создание OrderedDict с атрибутами задачи
        user_dict = OrderedDict()
        user_dict['id'] = self.id
        user_dict['name'] = self.name
        user_dict['surname'] = self.surname
        user_dict['position'] = self.position       
        
        return user_dict