import mysql.connector
import secrets
import base64
from flask import Flask, make_response, request, redirect
import hashlib,dbinit
from Crypto.Cipher import DES

app = Flask(__name__)


@app.route('/login/<username>/<password>', methods=['GET'])
def login(username,password):
    dbinit.db_init()
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="assignment"
    )
    try:
        cursor = mydb.cursor()
        statement = "SELECT username,password from users where username = '"+username+"' and password='"+password+"'"
        cursor.execute(statement)
        results = cursor.fetchall()
        if results:
            username_des = username
            if len(username) % 8 != 0:
                username_des = username + " "*(7-(len(username) % 8))
            token = token_update(cursor, username_des)
            token = username+"."+token
            mydb.commit()
            cursor.close()
            response = make_response(redirect('/index'))
            response.set_cookie('session_id', token)
            return response
        else:
            response = make_response("Login failed",400)
            cursor.close()
            return response
    except Exception as e:
        message = "<html><body><h1>Error occured during login process of user "+username+"</h1><p>Detail:" + str(e)+ "</p></body></html>"
        response = make_response(message,500)
        return response


def token_update(cursor,username):
    token = secrets.token_hex(16)
    statement = "INSERT INTO tokens(token_value) VALUES ('"+token+"')"
    cursor.execute(statement)
    token = username+"|"+token
    return des_encrypt(token)


def token_check(cursor, value):
    statement = "SELECT id from tokens where token_value = %s"
    data = [value.split('|')[1]]
    cursor.execute(statement, data)
    results = cursor.fetchall()
    if results:
        return True
    return False


def des_encrypt(value):
    password = "qwerty123"
    salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = password + salt
    m = hashlib.md5(key.encode('utf-8'))
    key = m.digest()
    (dk, iv) = (key[:8], key[8:])
    crypter = DES.new(dk, DES.MODE_CBC, iv)
    ciphertext = crypter.encrypt(value.encode('ascii'))
    return base64.b64encode(ciphertext).decode('ascii')


def des_decrypt(value):
    password = "qwerty123"
    salt = '\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'
    key = password + salt
    m = hashlib.md5(key.encode('utf-8'))
    key = m.digest()
    (dk, iv) = (key[:8], key[8:])
    crypter = DES.new(dk, DES.MODE_CBC, iv)
    encrypted_value = base64.b64decode(value.encode('ascii'))
    return crypter.decrypt(encrypted_value).decode('ascii')


@app.route('/index', methods=['GET'])
def index():
    try:
        mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
            database="assignment"
        )
        cursor = mydb.cursor()
        session_id_cookie = request.cookies.get('session_id').split('.')
        decrpyed_value = des_decrypt(session_id_cookie[1])
        if token_check(cursor,decrpyed_value):
            response_message = "<html><body><h1>Welcome "+decrpyed_value.split('|')[0]+"</h1></body></html>"
            response = make_response(response_message,200)
            return response
        return "{}"
    except Exception as e:
        print(e)
        message = "You dont have access to site"
        response = make_response(message,401)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
