from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'jk;adjio;asokj;cai;ohqwdj;xsmlkjquio'

from app import views
