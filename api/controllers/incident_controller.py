import psycopg2
import psycopg2.extras
from flask import jsonify, request

from api.helpers.auth import get_current_user
from api.helpers.mail_helper import status_emailing
from api.models.database_model import DatabaseConnection

db = DatabaseConnection()


def get_incidents_by_type(incident_type):
    sql_command = f"""SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents WHERE incident_Type='{incident_type}';"""
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchall()
    return incident


def get_incidents_by_id(incident_id, incident_type):
    sql_command = f"""SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents WHERE incident_Type='{incident_type}'
             AND incident_id='{incident_id}';"""
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchone()
    return incident


def get_incidents_by_status(incId, incident_type):
    data = request.get_json()
    incident = get_incidents_by_id(incident_type, incId)
    sql_command = f"""SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents WHERE status_='draft' AND 
            incident_id='{incId}';"""
    db.cursor.execute(sql_command)
    incident_status = db.cursor.fetchone()
    if not incident:
        return jsonify({"status": 404, "error": "Sorry, Incident Not Found"}), 404
    elif not incident_status:
        return jsonify({"status": 406, "Message": "Sorry, Update not Possible"}), 406
    elif not data:
        return jsonify({"status": 406, "message": "Sorry, No input value is inserted"}), 406


def create_incident(incident_type):
    data = request.get_json()
    sql_command = f"""INSERT INTO incidents (title,created_By,incident_Type,
        comment,status_,images,videos,created_On,latitude,longtitude)
        VALUES ('{data["title"]}','{get_current_user()["userId"]}',
        '{incident_type}','{data["comment"]}','draft','{data["images"]}',
        '{data["videos"]}',now(),'{data["latitude"]}','{data["longtitude"]}') RETURNING incident_id;"""
    try:
        db.cursor.execute(sql_command)
    except psycopg2.IntegrityError:
        return jsonify({"message": "Incident already exist"}), 406
    incident = db.cursor.fetchone()
    return incident


def update_incident_location(incident_Id, incident_type):
    data = request.get_json()
    sql_command = f"""UPDATE incidents SET (latitude,longtitude) = ('{data['latitude']}','{data['longtitude']}')
     WHERE incident_id='{int(incident_Id)}' AND incident_Type='{incident_type}' RETURNING incident_id;"""
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchall()
    return incident


def update_incident_comment(incident_Id, incident_type):
    data = request.get_json()
    sql_command = f"""UPDATE incidents SET comment = '{data['comment']}'
                WHERE incident_id='{incident_Id}' AND incident_Type='{incident_type}' RETURNING incident_id;"""
    db.cursor.execute(sql_command)

except psycopg2.IntegrityError:
return jsonify({"message": "Sorry, comments not accepted, make some change"}), 406
incident = db.cursor.fetchone()
return incident


def delete_incident(incident_Id, incident_type):
    sql_command = f"""DELETE FROM incidents WHERE incident_Id = '{incident_Id}' AND
             incident_Type= '{incident_type}' RETURNING incident_Id;"""
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchone()
    return incident


def update_incident_status(incident_Id, incident_type):
    data = request.get_json()
    sql_command = f"""UPDATE incidents SET status_ = '{data['status']}'
                WHERE incident_id='{incident_Id}' AND incident_Type='{incident_type}'
                 RETURNING incident_id;"""
    db.cursor.execute(sql_command)
    incident = db.cursor.fetchone()
    return incident


def mailme(myid):
    sql_command = f"""SELECT 
            users.user_Name,
            users.email,
            tbl_name.status_,
            tbl_name.incident_Id
        FROM incidents tbl_name
        LEFT JOIN users ON tbl_name.created_By=users.user_Id
        WHERE tbl_name.incident_Id='{myid}';"""
    db.cursor.execute(sql_command)
    me = db.cursor.fetchone()
    hello = status_emailing(me["email"], me["user_name"], me["incident_id"], me["status_"])
    return hello
