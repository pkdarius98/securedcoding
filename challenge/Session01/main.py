from flask import Flask, request, json, jsonify
import sqlite3
import re

app = Flask(__name__)

def get_db_connection(): 
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/product')
def search_products():
    query = request.args.get('query')
    if validate(query):
        return "bad request"

    conn = get_db_connection()
    
    try:
        sql = "SELECT * FROM products WHERE name like ?"
        result = conn.execute(sql, ['%' + query + '%']).fetchall()
        a = jsonify(result)
        return a
    except Exception as e:
        print("exception" + repr(e))
    finally:
        conn.close()
    return "error"

def validate(text):
    return re.match(r"^[0-9a-zA-z]+$", text) == None

app.run()