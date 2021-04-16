from typing import List, Dict
import simplejson as json
from flask import Flask, Response, render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'citiesData'
mysql.init_app(app)

@app.route('/', methods=['GET'])
def index():
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlb_players')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', mlb=result)

@app.route('/view/<int:mlb_id>', methods=['GET'])
def record_view(mlb_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlb_players WHERE id= %s', mlb_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', mlb=result[0])

@app.route('/edit/<int:mlb_id>', methods=['GET'])
def form_edit_get(mlb_id):
    print(mlb_id)
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM mlb_players WHERE id= %s', mlb_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', mlb=result[0])



if __name__ == '__main__':
    app.run(host='0.0.0.0')