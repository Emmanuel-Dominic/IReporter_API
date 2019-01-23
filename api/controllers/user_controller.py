from flask import jsonify,request
import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import psycopg2
import psycopg2.extras
from api.models.database_model import DatabaseConnection


db=DatabaseConnection()

def get_all_users():
    """docstring function that return all users detials"""
    sql_command="""SELECT * FROM users"""
    db.cursor.execute(sql_command)
    users=db.cursor.fetchall()
    return users


def signup_user():
    data = request.get_json()
    sql_command="""INSERT INTO users (first_Name,last_Name,other_Name,email,
            user_Name,phone_Number,passwd,isAdmin,joinning)
        VALUES ('{}','{}','{}',
            '{}','{}','{}','{}',FALSE, now()) RETURNING user_id,first_Name,last_Name,other_Name,email,
            user_Name,phone_Number,isAdmin,joinning;""".format(data["firstName"],
            data["lastName"],data["otherName"],
        data["email"],data["userName"],data["phoneNumber"],
        generate_password_hash(data["password"]))
    try:
        db.cursor.execute(sql_command)
    except psycopg2.IntegrityError:
        return jsonify({"message": "Email already in use"}),406
    user=db.cursor.fetchone()
    return user

def user_login_check():
    data = request.get_json()
    sql_command="""SELECT  passwd,email,user_Id FROM users WHERE email='{}'""".format(data["email"])
    db.cursor.execute(sql_command)
    user=db.cursor.fetchone()
    return user