"""views file for create, edit, get and delete redflad incidents"""
from flask import Blueprint, jsonify, request, Response, json
from app.models.incident_model import Incident


incident_bp = Blueprint('incident_bp', __name__, url_prefix='/api/v1')

incidents_db = [
    Incident(
        location={"locationLong":"0.39737", "locationLat":"9.38974"},
        # createdOn="2018-11-25 22:41:14",
        createdBy=2,
        type='redflag',
        # status="under_Investigation",
        images="1.jpeg",
        videos="1.gif",
        comment="Arnold was caught stilling jack fruit in hassan's Garden"
        ),
    Incident(
        location={"locationLong":"0.33737", "locationLat":"5.38974"},
        # createdOn="2018-08-24 02:31:14",
        createdBy=2,
        type='intervention',
        # status="resolved",
        images="2.jpeg",
        videos="2.gif",
        comment="Malamba highway needs construction because it's in bad state and it's also causing alot of accidents"
        ),
    Incident(
        location={"locationLong":"0.39737", "locationLat":"9.38974"},
        # createdOn="2018-11-25 22:41:14",
        createdBy=2,
        type='redflag',
        # status="rejected",
        images="3.jpeg",
        videos="3.gif",
        comment="Hussien knocked moses's cow along masaka road, he was drank"
        )
        ]



@incident_bp.route('/redflags', methods=['GET'])
def get_all_redflags():
    """docstring function that return all redflags detials"""
    redflags_list = []
    for record in incidents_db:
        if record.type == 'redflag':
            redflags_list.append(record.get_incident_details())
    if redflags_list:
        return jsonify({
            "status": 200,
            "data": redflags_list
        }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200
