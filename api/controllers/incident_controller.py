import psycopg2
import psycopg2.extras
import datetime
from flask import jsonify, request
from api.helpers.mail_helper import status_emailing
from api.helpers.auth import get_current_user
from api.models.database_model import DatabaseConnection

db = DatabaseConnection()


def get_incidents_by_type(incident_type):
    sql_command = """SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents WHERE incident_Type='{}';""".format(incident_type)
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchall()
    return incident


def get_incidents_by_id(incident_id):
    sql_command = """SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents WHERE incident_id={};""".format(incident_id)
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchone()
    return incident


def get_incidents_by_status(incId):
    data = request.get_json()
    incident = get_incidents_by_id(incId)
    sql_command = """SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents WHERE status_='{}' AND 
            incident_id={}""".format('draft', incId)
    db.cursor.execute(sql_command)
    incident_status = db.cursor.fetchone()
    if not incident:
        return jsonify({"status": 404, "error": "Sorry, Incident Not Found"}), 404
    elif not incident_status:
        return jsonify({"status": 406, "Message": "Sorry, Update not Possible"}), 406
    elif not data:
        return jsonify({"status": 406, "message": "Sorry, No input value is inserted"}), 406


def create_incident():
    data = request.get_json()
    sql_command = """INSERT INTO incidents (title,created_By,incident_Type,
        comment,status_,images,videos,created_On,latitude,longtitude)
        VALUES ('{}','{}','interventon','{}','draft','{}','{}',now(),
        '{}','{}') RETURNING incident_id""".format(data["title"],
                                                   get_current_user()["userId"],
                                                   data["comment"], data["images"], data["videos"], data["latitude"],
                                                   data["longtitude"])
    try:
        db.cursor.execute(sql_command)
    except psycopg2.IntegrityError:
        return jsonify({"message": "Incident already exist"}), 406
    incident = db.cursor.fetchone()
    return incident


def update_incident_location(incident_Id):
    data = request.get_json()
    sql_command = """UPDATE incidents SET (latitude,longtitude) = ('{}','{}')
                WHERE incident_id='{}' RETURNING incident_id""".format(
        float(data['latitude']), float(data['longtitude']),
        int(incident_Id))
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchall()
    return incident


def update_incident_comment(incident_Id):
    data = request.get_json()
    sql_command = """UPDATE incidents SET comment = '{}'
                WHERE incident_id='{}' RETURNING incident_id""".format(
        str(data['comment']), int(incident_Id))
    try:
        db.cursor.execute(sql_command)
    except psycopg2.IntegrityError:
        return jsonify({"message": "Sorry, comments not accepted, make some change"}), 406
    incident = db.cursor.fetchone()
    return incident


def delete_incident(incident_Id,incident_Type):
    sql_command = """DELETE FROM incidents WHERE incident_Id = '{}' AND
             incident_Type= '{}' RETURNING incident_Id
             """.format(incident_Id,incident_Type)
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchone()
    return incident


def update_incident_status(incident_Id):
    data = request.get_json()
    sql_command = """UPDATE incidents SET status_ = '{}'
                WHERE incident_id='{}' RETURNING incident_id""".format(
        str(data['status']), int(incident_Id))
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchone()
    return incident


def mailme(myid):
    sql_command = """SELECT 
            users.user_Name,
            users.email,
            tbl_name.status_,
            tbl_name.incident_Id
        FROM incidents tbl_name
        LEFT JOIN users ON tbl_name.created_By=users.user_Id
        WHERE tbl_name.incident_Id={}""".format(int(myid))
    db.cursor.execute(sql_command)
    me = db.cursor.fetchone()
    hello = status_emailing(me["email"], me["user_name"], me["incident_id"], me["status_"])
    return hello
