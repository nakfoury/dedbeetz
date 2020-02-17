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
import logging
import os
import urllib.request

import jinja2
from flask import Flask, request, render_template
from google.cloud import storage

storage_client = storage.Client()

UPLOAD_FOLDER = 'beetz/'

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.jinja_loader = jinja2.FileSystemLoader('vue/dist')


def allowed_file(file):
    return True


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def vue_client(path):
    logging.info(path)
    # Production mode - serve static built files
    if os.getenv('GAE_ENV', '').startswith('standard'):
        return render_template('index.html')
    # Dev mode - proxy the vue dev server
    else:
        url = f'http://localhost:3000/{path}'
        logging.error(url)
        return urllib.request.urlopen(url).read()


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['fileToUpload']
    if f and allowed_file(f):
        bucket = storage_client.get_bucket("dedbeetz-media")
        blob = bucket.blob('beetz/' + f.filename)
        blob.upload_from_file(f)
        file_url = blob.generate_signed_url(expiration=datetime.timedelta(seconds=30))
    return file_url


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
