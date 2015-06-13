# all the imports

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from flaskext.mysql import MySQL
from flask.ext.scss import Scss

# configuration
DATABASE = '/tmp/app.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
mysql = MySQL()
app = Flask(__name__)
Scss(app, static_dir='static', asset_dir='assets')
app.config.from_object(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'nbascrape'
mysql.init_app(app)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def show_entries():
    cur = mysql.get_db().cursor()
    cur.execute("select player_id, 2013_14 from player_salary limit 5")
    entries = [dict(player=row[0], salary=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

if __name__ == '__main__':
    app.run()