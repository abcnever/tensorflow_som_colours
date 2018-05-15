from flask import Flask
from flask_cors import CORS
from flask_caching import Cache

app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

from app import routes
