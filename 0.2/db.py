import json
import mysql.connector


class DB:
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

    def close_connection(self):
        self.db.close()

    def get_all_tasks(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task")
        result = cursor.fetchall()
        self.db.commit() 
        cursor.close()
        return result    

    def get_task_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM task WHERE id = %s", (id,))
        result = cursor.fetchall()
        self.db.commit() 
        cursor.close()
        return result    

    def add_task(self, title, description):
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO task (title, description) VALUES (%s, %s)", (title, description))
        self.db.commit()
        task_id = cursor.lastrowid
        cursor.close()
        return task_id

    def update_task(self, id, status):
        cursor = self.db.cursor()
        cursor.execute("UPDATE task SET status=%s WHERE id=%s", (status, id))
        self.db.commit()
        cursor.close()
        return f'Task {id}, status changed to {status}'

    def delete_task_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM task WHERE  id=%s", (id,))
        self.db.commit() 
        cursor.close()
        return f'Task {id}, deleted from DB'
