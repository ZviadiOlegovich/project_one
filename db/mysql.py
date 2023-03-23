import json
import mysql.connector
from app.storage import Storage
from app.task import Task

class Database(Storage):
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            config = json.load(f)

        self.db = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database'],
            port=config['port']
        )

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
        result = cursor.fetchall()
        self.db.commit() 
        cursor.close()
        print(result[0][3])
        return result    

    def insert_task(self, task: Task):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO task (title, description) VALUES (%s, %s)", 
                       (task.title, task.description))
        self.db.commit()
        task_id = cursor.lastrowid
        cursor.close()
        return task_id

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