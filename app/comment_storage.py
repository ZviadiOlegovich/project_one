from app.comment_interface import CommentStorage
from app.comment import Comment
from datetime import datetime

class CommentDb(CommentStorage):
    def __init__(self, connect):
        self.db = connect
        
    def get_comment(self, id: int) -> list:
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM comment WHERE task_id = %s", (id,))
        ans = cursor.fetchall()
        comments =[Comment(*c) for c in ans]
        self.db.commit() 
        cursor.close()               
        return comments 
        
    def add_comment(self, comment: Comment) -> Comment: # notify
        cursor = self.db.cursor()
        comment.d_time = datetime.now()
        cursor.execute("INSERT INTO comment (task_id, message, date_time) VALUES (%s, %s, %s)", 
                       (comment.task_id, comment.message, comment.d_time))
        self.db.commit()
        comment.id = cursor.lastrowid        
        cursor.close()
        return comment