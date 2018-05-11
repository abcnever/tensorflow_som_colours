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


files = [
            "app/static/data/0.png",
            "app/static/data/1.png",
            "app/static/data/2.png",
            "app/static/data/3.png"
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
    hex_colours = request.json
    rgb_colours = []
    global cached_colours
    for colour in hex_colours:

        rgb_colours.append(
                list(map(lambda x: x / 255,
                    list(webcolors.hex_to_rgb(colour))
                ))
            )

    # print(hex_colours)
    rgb_colours = np.asarray(rgb_colours)

    print("Starting thread to train")
    t = Thread(target=process_som_model, args=(rgb_colours,))
    t.start()

    # output_data = model_api(input_data)
    # response = jsonify(output_data)
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

        return render_template("api_polling.html", images=relative_pathes)
    else:
        return render_template("empty_content.html")

