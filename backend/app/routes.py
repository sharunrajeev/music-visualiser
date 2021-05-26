from app.visualiser import start_visuals
from app import app
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template
import os

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello world</h1>"


@app.route("/music", methods=['GET', 'POST'])
def visualize():
    if request.method == 'POST':
        print("file ready for uploading")
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join('./save/', filename))
    start_visuals(filename)
    return "<h2>Visualizing please wait</h2>"

