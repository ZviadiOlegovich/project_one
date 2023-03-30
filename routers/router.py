from flask import jsonify, request
from app.app import App
from app.task import Task
from app.comment import Comment
from datetime import datetime
import sys
import traceback

class TaskRoutes:
    def __init__(self, app: App, router):
        self.app = app
        self.router = router
        self.register_routes()

    def register_routes(self):
        self.router.route('/', methods=['GET'], endpoint='index')(self.index)
        self.router.route('/data/', methods=['GET'], endpoint='get_all_tasks')(self.get_all_tasks)
        self.router.route('/data/<int:id>', methods=['GET'], endpoint='get_task_by_id')(self.get_task_by_id)
        self.router.route('/data', methods=['POST'], endpoint='insert_task')(self.insert_task)
        self.router.route('/data/<int:id>', methods=['PUT'], endpoint='update_task')(self.update_task)
        self.router.route('/data/<int:id>', methods=['DELETE'], endpoint='delete_task')(self.delete_task)
        self.router.route('/data/sort/<string:status>', methods=['GET'], endpoint='sort_by_status')(self.sort_by_status)
        self.router.route('/comment/<int:id>', methods=['GET'], endpoint='get_comments_by_id')(self.get_comments_by_id)
        self.router.route('/comment', methods=['POST'], endpoint='insert_comment')(self.insert_comment)

    
    
    
    def get_comments_by_id(self, id):
        try:            
            comments = self.app.get_comments_by_id(id)
            return [comment.to_json() for comment in comments]
        except Exception:
            ans = f"comment {id} - not found1"
            return handling_exceptions(ans)
        
    def insert_comment(self):
        try:
            task_id = request.json.get('task_id')
            message = request.json.get('message')
            comment = Comment(0, task_id, message)
            result = self.app.insert_comment(comment)
            return jsonify(result)
        except Exception:
            return handling_exceptions('insert_comment')
        
         
    def sort_by_status(self, status):
        try:
            tasks = self.app.sort_by_status(status)
            return jsonify(tasks)

        except Exception:
            return handling_exceptions()   

    def index(self):
        return self.app.info()

    def get_all_tasks(self):
        try:
            tasks = self.app.find_tasks()
            return [task.to_json() for task in tasks]

        except Exception:
            return handling_exceptions('all')
        

    def get_task_by_id(self, id):
        try:            
            task = self.app.find_task_by_id(id)
            return task.to_json()
        except Exception:
            ans = f"task {id} - not found1"
            return handling_exceptions(ans)


    def insert_task(self):
        try:
            title = request.json.get('title')
            description = request.json.get('description')
            task = Task(0, title, description)
            result = self.app.create_new_task(task)
            return jsonify(result)
        except Exception:
            return handling_exceptions('insert')

    def update_task(self, id):
        try:
            title = request.json.get('title')
            description = request.json.get('description')
            status = request.json.get('status')
            task = Task(id, title, description, status)
            result = self.app.update_task(task)
            return jsonify(result)
        except Exception:
            return handling_exceptions('update')

    def delete_task(self, id):
        try:
            result = self.app.delete_task_by_id(id)
            return jsonify({'result': result})
        except Exception:
            return handling_exceptions('delete')

    def response_error(self):
        pass

def handling_exceptions(str):
    e = sys.exc_info()[1]            
    with open('data\logs.log', 'a') as lf:
        tm = datetime.now()
        lf.write(F"Time: {tm}; Error: {e}\n")
        traceback.print_exc(file=lf)
             
    return "Sorry, " + str , 500


#     @router.errorhandler(404)
# def pageNotFound(error):
#     with open('log_file.txt', 'a') as lf:
#         tm = datetime.now()
#         lf.write(F"inputed incorrect URL ({tm})\n")
#     return "Page not found, please input correct URL"
