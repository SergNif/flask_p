from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = '54.38.176.15'
app.config['MYSQL_DATABASE_USER'] = 'flask'
app.config['MYSQL_DATABASE_PASSWORD'] = 'svgSD#201'
app.config['MYSQL_DATABASE_DB'] = 'flask'

mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def index():
    cur = mysql.get_db().cursor()

    cur.execute("SELECT * FROM `tbl_user` WHERE 1")
    rv = cur.fetchall()
    return str(rv)


if __name__ == '__main__':
    app.run()
