# from dedbeetz.wsgi import application

# App Engine by default looks for a main.py file at the root of the app
# directory with a WSGI-compatible object called app.
# This file imports the WSGI-compatible object of your Django app,
# application from dedbeetz/wsgi.py and renames it app so it is discoverable by
# App Engine without additional configuration.
# Alternatively, you can add a custom entrypoint field in your app.yaml:
# entrypoint: gunicorn -b :$PORT dedbeetz.wsgi
# app = application


import datetime
import magic

import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from google.cloud import storage
storage_client = storage.Client()




UPLOAD_FOLDER = 'beetz/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(file):
    return True


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    f = request.files['fileToUpload']
    if f and allowed_file(f):
        bucket = storage_client.get_bucket("dedbeetz-media")
        blob = bucket.blob(f.filename)
        blob.upload_from_file(f)
        # f.save(os.path.join('gs://dedbeetz-media', app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    return render_template('index.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
