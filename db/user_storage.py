from interfaces.user_st_interface import UserStorage
from entities.user import User


class UserDb(UserStorage):
    def __init__(self, connect):
        self.db = connect
        
    def get_user_by_id(self, id: int) -> User:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM user WHERE id = %s", (id,))
        args = cursor.fetchall()[0]   
        user = User(*args)     
        self.db.commit() 
        cursor.close()               
        return user 
        
    def insert_user(self, user: User) -> User: # notify
        cursor = self.db.cursor()        
        cursor.execute("INSERT INTO user (name, surname, position) VALUES (%s, %s, %s)", 
                       (user.name, user.surname, user.position))
        self.db.commit()
        user.id = cursor.lastrowid        
        cursor.close()
        return user
    
    
    def delete_user_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM user WHERE  id=%s", (id,))
        self.db.commit() 
        cursor.close()
        return 