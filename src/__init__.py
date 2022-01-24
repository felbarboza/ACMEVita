from turtle import dot
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(os.getenv('postgres_user'), os.getenv('postgres_password'), os.getenv('postgres_host'), os.getenv('postgres_port'), os.getenv('postgres_name'))
db = SQLAlchemy(app)
