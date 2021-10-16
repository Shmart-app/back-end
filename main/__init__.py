from flask import Flask
from flask import request
import sqlite3
from flask import g
import json
app = Flask(__name__)

from product_api import routes
from nutrition_api import routes
from customer_rating_api import routes