from flask import Flask, request

app = Flask(__name__)

if hasattr(request, 'cache_control'):
    print('cache_control is available in Flask version', Flask.__version__)
else:
    print('cache_control is not available in Flask version', Flask.__version__)