import json
import mysql.connector


def connect_to_db(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)

    db = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database'],
        port=config['port']
    )

    return db


def get_all_tasks(db):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task")
    result = cursor.fetchall()
    db.commit() 
    cursor.close()
    return result    


def get_task_by_id(db, id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM task WHERE id = %s", (id,))
    result = cursor.fetchall()
    db.commit() 
    cursor.close()
    return result    


def add_task(db, title, description):
    cursor = db.cursor()
    cursor.execute("INSERT INTO task (title, description) VALUES (%s, %s)", (title, description))
    db.commit()
    task_id = cursor.lastrowid
    cursor.close()
    return task_id


def update_task(db, id, status):
    cursor = db.cursor()
    cursor.execute("UPDATE task SET status=%s WHERE id=%s", (status, id))
    db.commit()
    cursor.close()
    return f'Task {id}, status changed to {status}'


def delete_task_by_id(db, id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM task WHERE  id=%s", (id,))
    db.commit() 
    cursor.close()
    return f'Task {id}, deleted from DB'  