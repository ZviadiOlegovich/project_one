import http.server
import socketserver
import json
import mysql.connector

# Подключение к базе данных
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ford2008",
    database="todo",
    port="33306",
)

# Создание курсора для выполнения запросов
cursor = db.cursor()


PORT = 8000

class MyAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response code and headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = {'message': 'Hello, world!'}

        query = "SELECT * FROM tasks"
        cursor.execute(query)
        tasks = cursor.fetchall()
        # //if len(tasks) > 0:
        response = {'tasks': tasks}
        # //else:
        #   //  response = {'message': "the list is empty"}

        # Construct and send the response
        
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        # Get the request body
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        

        # Parse the JSON request body
        request = json.loads(body)

        # Construct the response
        response = {'message': f'Hello, {request.get("name", "world")}!'}

        # Set response code and headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Send the response
        self.wfile.write(json.dumps(response).encode())

# Create the server and bind it to the specified port
with socketserver.TCPServer(("", PORT), MyAPIHandler) as httpd:
    print("serving at port", PORT)

    # Serve HTTP requests until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()