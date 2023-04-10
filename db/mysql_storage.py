# import mysql.connector
from datetime import datetime
from interfaces.mysql_interface import Storage
from entities.task import Task


class MySQLDb(Storage):
    def __init__(self, connect):
        self.db = connect
        

    def info(self):
        return "storage info"

    def get_all_tasks(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task")
        ans = cursor.fetchall()
        tasks = [Task(*t) for t in ans]
        self.db.commit() 
        cursor.close()
        return tasks    

    def get_task_by_id(self, id: int) -> Task:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task WHERE id = %s", (id,))
        args = cursor.fetchall()[0]             
        task = Task(*args)
        self.db.commit() 
        cursor.close()               
        return task   

    def insert_task(self, task: Task) -> Task:
        start_time = datetime.now()
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO task (title, description, author, assignee, start_time) VALUES (%s, %s, %s, %s, %s)", 
                       (task.title, task.description, task.author, task.assignee, start_time))
        self.db.commit()
        task.id = cursor.lastrowid
        cursor.close()
        return task

    def update_task(self, task: Task):        
        if task.status == 'done':
            task.end_time =  datetime.now()
        cursor = self.db.cursor()
        cursor.execute("UPDATE task SET title = %s, description = %s, status=%s, end_time=%s WHERE id=%s", 
                       (task.title, task.description, task.status, task.end_time, task.id))
        self.db.commit()
        cursor.close()
        return 

    def delete_task_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM task WHERE  id=%s", (id,))
        self.db.commit() 
        cursor.close()
        return 


    def get_sorted_task(self, status: str):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task WHERE status = %s", (status,))
        result = cursor.fetchall()
        self.db.commit() 
        cursor.close()
        return result
    
    
    def close_connection(self):
        self.db.close()