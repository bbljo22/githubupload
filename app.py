# Import Libraries
from flask import Flask,render_template

# Define app.
app = Flask(__name__)

# Import the __init__.py from modules which had imported all files from the folder.
import modules
