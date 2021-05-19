from app import app
from app import visualiser
import time

@app.route("/")
@app.route("/home")
def home():
    return "Hello World"

@app.route("/time")
def get_time():
    return {'time': time.time()}

@app.route("/music")
def show_music():
    visualiser.start_visualiser()
    return "Hello Music"
