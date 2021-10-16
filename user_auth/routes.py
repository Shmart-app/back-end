from main import app
from main import request
from main import json
from flask import g
from main import sqlite3

# Expects a request body of type
# {
# username: "myuser", 
# password: "mypass", 
# fullname: "myfullname"
# number: 1234567890
# }

@app.route('/user/register', methods=['POST'], endpoint='userregister')
def userregister():
    try: 
        data = json.loads(request.data)

        username = data["username"]
        pw = data["password"]
        name = data["fullname"]
        number = int(data["number"])

        conn = sqlite3.connect('sql/customers.db')
        print(f'got json values, {username}, {pw}, {name}, {number}')
        print(conn)
        curs = conn.cursor()

        user = curs.execute("SELECT * FROM users WHERE username = ?", (username, ))
        check = user.fetchone()
        print(check)
        print('queried db')

        if check is None: #if username does not exist in the table, add it
            curs.execute('INSERT INTO users (username, password, fullname, number) VALUES (?, ?, ?, ?)', (username, pw, name, number))
            conn.commit()
            response = app.response_class(
                response=json.dumps({"message":"User successfully registered."}),
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            print('Username already exists')
            response = app.response_class(
                response=json.dumps({"message":"The selected username already exists, please choose another one"}),
                status=409,
                mimetype='application/json'
            )
            return response        
    except Exception as e:
        print(e)
        response = app.response_class(
            response=json.dumps({"message":"The server encountered an error with your request"}),
            status=403,
            mimetype='application/json'
        )
        return response

#Login
@app.route('/user/login', methods=['POST'], endpoint='userlogin')
def userlogin():
    try: 
        pass
    except:
        response = app.response_class(
            response=json.dumps({"message":"The server encountered an error with your request"}),
            status=403,
            mimetype='application/json'
        )
        return response



DATABASE = 'sql/customers.db'



@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv