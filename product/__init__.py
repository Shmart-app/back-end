from flask import Flask
from flask import request
import json
app = Flask(__name__)

from product import routes
