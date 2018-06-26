from flask import Flask, render_template
import app.controllers
import pymongo
from pymongo import MongoClient

app = Flask(__name__, template_folder='template')

app.config.from_object('config')

client = MongoClient('localhost', 27017)

# db = client.sampleDB