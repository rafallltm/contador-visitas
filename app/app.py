from flask import Flask, request
import socket

app = Flask(__name__)
visit_count = 0

@app.route('/')
def hello_world():
    global visit_count
    visit_count += 1
    host_name = socket.gethostname()
    return f'Hello! You are visiting from {host_name}. This page has been visited {visit_count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
