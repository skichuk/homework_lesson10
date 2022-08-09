from flask import Flask
import json

with open('candidates.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

app = Flask(__name__)
