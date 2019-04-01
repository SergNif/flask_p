from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash


mysql = MySQL()
appFlask = Flask(__name__)

# MySQL configurations
appFlask.config['MYSQL_DATABASE_USER'] = 'flask'
appFlask.config['MYSQL_DATABASE_PASSWORD'] = 'svgSD#201'
appFlask.config['MYSQL_DATABASE_DB'] = 'flask'
appFlask.config['MYSQL_DATABASE_HOST'] = '54.38.176.15'
mysql.init_app(appFlask)



@appFlask.route("/")
def main():
    return render_template('index.html')


@appFlask.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@appFlask.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # validate the received values
        if _name and _email and _password:
            
            # All Good, let's call MySQL
            
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close() 
        conn.close()

@appFlask.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from tbl_user where user_name='" + username + "' and user_password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"


if __name__ == "__main__":
    appFlask.run()
#
#
# db = MySQLdb.connect(
#    host="54.38.176.15",
#    user="flask",
#    passwd="svg#SD201",
#    db="flask",
#    charset='utf8')
#
#cursor = db.cursor()
