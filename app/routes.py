from app import app
from flask import Flask, request, jsonify, make_response, render_template
import webcolors
from app.serve import process_som_model
from threading import Thread
from pathlib import Path
import numpy as np
import contextlib
import os
import re
import time


files = [
            "app/static/data/0.png",
            "app/static/data/1.png",
            "app/static/data/2.png",
            "app/static/data/3.png",
            "app/static/data/4.png"
            ]

@app.route('/')
def index():
    return render_template("index.html")

# HTTP Errors handlers
@app.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@app.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

# request this route to start the training
@app.route('/api', methods=['POST'])
def api():
    hex_colours = request.form.getlist('colors')
    app.logger.info(str(request.form))

    x_dim = int(request.form['x-dim'])
    y_dim = int(request.form['y-dim'])


    rgb_colours = []
    global files

    for file in files:
        if Path(file).is_file():
            Path(file).unlink()

    for colour in hex_colours:
        rgb_colours.append(
                list(map(lambda x: x / 255,
                    list(webcolors.hex_to_rgb(colour))
                ))
            )

    rgb_colours = np.asarray(rgb_colours)

    app.logger.info("Starting a thread to train the model")
    t = Thread(target=process_som_model, args=(rgb_colours,x_dim, y_dim,))
    t.start()

    response = jsonify([])
    return response

# ajax polling this route to load the training result
@app.route('/api_polling', methods=['GET'])
def api_polling():
    all_exist = True
    global files

    for file in files:
        if not (Path(file).is_file()):
            all_exist = False

    if all_exist:
        relative_pathes = []

        for file in files:
            relative_pathes.append(re.sub('app/static/', '', file))

        # invalidate the cache mechanism. so the images are always the newest
        response = make_response(render_template("api_polling.html", images=relative_pathes, timestamp=str(time.time())))
        response.cache_control.max_age = 0
        return response

    else:
        return render_template("empty_content.html")

