from flask import Flask, jsonify
from flask import request
import psycopg2.extras
from helper import *


app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_all_employees():
    employees = []
    try:
        cur = psql_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("Select * from accounts")
        employees = cur.fetchall()
        cur.close()
        response = get_error_msg("get")
    except Exception as e:
        response = get_error_msg("get", "error")
    return jsonify({"data":employees, "response":response})

@app.route("/get/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    try:
        cur = psql_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("Select * from accounts where id = {}".format(emp_id))
        employees = cur.fetchone()
        response = get_error_msg("get")
    except Exception as e:
        response = get_error_msg("get", "error")
    return jsonify({"data":employees, "response":response})

@app.route("/add/emp", methods=["POST"])
def add_employee():
    try:
        emp = request.json
        if emp.get("name"): 
            cur = psql_connection.cursor()
            query = "insert into accounts (name, age) values ('%s', '%s')" % (emp.get("name"), emp.get("age"))
            cur.execute(query)
            cur.close()
            response = get_error_msg("post")
        else:
            response = 400
    except Exception as e:
        print(str(e))
        # response = get_error_msg("post", "error")
        response = str(e)
    return jsonify({"data":[], "response":response})

@app.route("/update/emp", methods=["PATCH", "PUT"])
def update_employee():
    try:
        emp = request.json
        query_builder, emp_id = "", ""
        for key, value in emp.items():
            if key == "id":
                emp_id = value
            else:
                query_builder += key + "=" +"'"+value+"'"+","
        cur = psql_connection.cursor()
        query = "update accounts set {fields} where id = {id}".format(fields=query_builder[:-1],id=emp_id)
        cur.execute(query)
        cur.close()
        response = get_error_msg("post")
    except Exception as e:
        response = get_error_msg("post", "error")
    return jsonify({"data":[], "response":response})

@app.route("/delete/emp/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    try:
        cur = psql_connection.cursor()
        query = "Delete from accounts where id = {}".format(emp_id)
        cur.execute(query)
        cur.close()
        response = get_error_msg("post")
    except Exception as e:
        response = get_error_msg("post", "error")
    return jsonify({"data":[], "response":response})


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5001, debug=True)


