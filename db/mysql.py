# import mysql.connector
from app.storage import Storage
from app.task import Task

class MySQLdb(Storage):
    def __init__(self, connect):
        self.db = connect
        

    def info(self):
        return "storage info"

    def get_all_tasks(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task")
        result = cursor.fetchall()
        self.db.commit() 
        cursor.close()
        return result    

    def get_task_by_id(self, id: int) -> Task:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task WHERE id = %s", (id,))
        r = cursor.fetchall()
        task = Task(r[0][0],r[0][1],r[0][2],r[0][3])
        self.db.commit() 
        cursor.close()               
        return task   

    def insert_task(self, task: Task) -> Task:
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO task (title, description) VALUES (%s, %s)", 
                       (task.title, task.description))
        self.db.commit()
        task.id = cursor.lastrowid
        cursor.close()
        return task

    def update_task(self, task: Task):
        cursor = self.db.cursor()
        cursor.execute("UPDATE task SET title = %s, description = %s, status=%s WHERE id=%s", 
                       (task.title, task.description, task.status, task.id))
        self.db.commit()
        cursor.close()
        return 

    def delete_task_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM task WHERE  id=%s", (id,))
        self.db.commit() 
        cursor.close()
        return 

    def close_connection(self):
        self.db.close()