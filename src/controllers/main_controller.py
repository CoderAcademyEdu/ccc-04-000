from flask import Blueprint, request, abort, jsonify, current_app
import socket

main = Blueprint('main', __name__, url_prefix="")

count = 0

@main.route("/", methods=["GET"])
def index():
    global count 
    count += 1
    return f"""
    <h1>Server IP is {socket.gethostbyname(socket.gethostname())}</h1>
    <p>Current view count is {count}</p>
    <p>MY_ENV value - {current_app.config['MY_ENV']}</p>
    """