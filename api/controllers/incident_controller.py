import psycopg2
import psycopg2.extras
import datetime
from flask import jsonify,request
from api.helpers.mail_helper import status_emailing
from api.helpers.auth import get_current_user
from api.models.database_model import DatabaseConnection


db =DatabaseConnection()


def get_incidents_by_type(incident_type):
    sql_command="""SELECT incident_id,title,created_by,'{}',
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM incidents;""".format(incident_type)
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchall()
    return incident

def get_incidents_by_type_id(incident_type,incident_id):
    sql_command="""SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM {} WHERE incident_id={};""".format(incident_type,incident_id)
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchone()
    return incident

def get_incidents_by_status(incident_type,incId):
    data=request.get_json()
    incident=get_incidents_by_type_id(incident_type,incId)
    sql_command="""SELECT incident_id,title,created_by,incident_Type,
            comment,status_,images,videos,created_On,latitude,
            longtitude FROM {} WHERE status_='{}' AND 
            incident_id={}""".format(incident_type,'draft',incId)
    db.cursor.execute(sql_command)
    incident_status=db.cursor.fetchone()
    if not incident:
        return jsonify({"status":404,"error": "Sorry, Incident Not Found"}),404
    elif not incident_status:
        return jsonify({"status":406,"Message": "Sorry, Update not Possible"}),406
    elif not data:
        return jsonify({"status":406,"message":"Sorry, No input value is inserted"}),406


def create_incident(incident_type):
    data = request.get_json()
    sql_command="""INSERT INTO {} (title,created_By,incident_Type,
        comment,status_,images,videos,created_On,latitude,longtitude)
        VALUES ('{}','{}','interventon','{}','draft','{}','{}',now(),
        '{}','{}') RETURNING incident_id""".format(incident_type,data["title"],get_current_user()["userId"],
        data["comment"],data["images"],data["videos"],data["latitude"],data["longtitude"])
    try:
        db.cursor.execute(sql_command)
    except psycopg2.IntegrityError:
        return jsonify({"message": "Incident already exist"}),406
    incident=db.cursor.fetchone()
    return incident


def update_incident_location(incident_type,incident_Id):
    data = request.get_json()
    sql_command="""UPDATE {} SET (latitude,longtitude) = ('{}','{}')
                WHERE incident_id='{}' RETURNING incident_id""".format(incident_type,
                float(data['latitude']),float(data['longtitude']),int(incident_Id))
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchall()
    return incident   


def update_incident_comment(incident_type,incident_Id):
    data = request.get_json()
    sql_command="""UPDATE {} SET comment = '{}'
                WHERE incident_id='{}' RETURNING incident_id""".format(incident_type,
                str(data['comment']),int(incident_Id))
    try:
        db.cursor.execute(sql_command)
    except psycopg2.IntegrityError:
        return jsonify({"message": "Sorry, comments not accepted, make some change"}),406
    incident=db.cursor.fetchone()
    return incident


def delete_incident(incident_tpye,incident_Id):
    sql_command="""DELETE FROM {} WHERE incident_Id = '{}'
             RETURNING incident_Id""".format(incident_tpye,int(incident_Id))
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchone()
    return incident


def update_incident_status(incident_type,incident_Id):
    data = request.get_json()
    sql_command="""UPDATE {} SET status_ = '{}'
                WHERE incident_id='{}' RETURNING incident_id""".format(incident_type,
                str(data['status']),int(incident_Id))
    db.cursor.execute(sql_command)
    incident=db.cursor.fetchone()
    return incident


def mailme(incident_type,myid):
    sql_command="""SELECT 
            users.user_Name,
            users.email,
            tbl_name.status_,
            tbl_name.incident_Id
        FROM {} tbl_name
        LEFT JOIN users ON tbl_name.created_By=users.user_Id
        WHERE tbl_name.incident_Id={}""".format(incident_type,int(myid))
    db.cursor.execute(sql_command)
    me = db.cursor.fetchone()
    hello=status_emailing(me["email"],me["user_name"],me["incident_id"],me["status_"])
    return hello
  

