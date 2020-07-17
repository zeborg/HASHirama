import os
import hashlib
from flask import Flask

app = Flask(__name__)

MAX_FILE_SIZE_MB = 50
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADS_FOLDER'] = os.path.join(APP_ROOT, 'static/uploads')
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE_MB * 1024 * 1024

app.config['SECRET_KEY'] = 'Shhh...'

from HASHirama import routes
