"""views file for create, edit, get and delete redflad incidents"""
from flask import Blueprint, jsonify, request, Response, json
from api.models.incident_model import Incident

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
        comment="Arnold was caught stealing jack fruit in hassan's Garden"
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
        comment="Hussien knocked moses's cow along masaka road, 'he was drank'"
        )
        ]



@incident_bp.route('/')
def index():
    try:
        return jsonify({'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}), 200
    except 404:
        return jsonify({'url_prefix': 'Please include api/v1/ on the ulr'}), 200



@incident_bp.route('/redflags', methods=['GET'])
def get_all_redflags():
    """docstring function that return all redflags detials"""
    redflags_list = []
    for record in incidents_db:
        if record.type == "redflag":
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



@incident_bp.route('/redflags/<int:redFlagId>', methods=['GET'])
def get_specific_redflag(redFlagId):
    for record in incidents_db:
        if record.type == 'redflag' and record.incidentId == redFlagId:
            return jsonify({
                "status": 200,
                "data": record.get_incident_details()
            }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@incident_bp.route('/redflags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    if data:
        location = {"locationLong":data["locationLong"], "locationLat":data["locationLat"]}
        newIncident=Incident(location=location, createdBy=data['createdBy'],\
            type=data['type'], images=data['images'], videos=data['videos'],\
            comment=data['comment'])
        incidents_db.append(newIncident)
        return jsonify({
            "status": 200,
            "data":[{
                "id":incidents_db[-1].incidentId,
                "message": "Created red-flag record"}]
        }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 400


@incident_bp.route('/redflags/<int:redFlagId>/location', methods=['PATCH'])
def update_redflag_location(redFlagId):
    for incident in incidents_db:
        if incident.type == 'redflag' and incident.incidentId == redFlagId:
            data = request.get_json()
            location = {"locationLong":data['locationLong'], "locationLat":data['locationLat']}
            incident.set_location(location)
        return jsonify({
            "status": 200,
            "data":[{
                "id":  incident.incidentId,
                "message": "Updated red-flag record's location"}]
        }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@incident_bp.route('/redflags/<int:redFlagId>/comment', methods=['PATCH'])
def update_redflag_comment(redFlagId):
    for record in incidents_db:
        if record.type == 'redflag' and record.incidentId == redFlagId:
            data = request.get_json()
            comment = data['comment']
            record.set_comment(comment)
        return jsonify({
            "status": 200,
            "data":[{
                "id":  record.get_incident_details(),
                "message": "Updated red-flag record's comment"}]
        }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@incident_bp.route('/redflags/<int:redFlagId>', methods=['DELETE'])
def delete_redflag(redFlagId):
    for record in incidents_db:
        if record.incidentId == 'redFlagId' and record.incidentId == redFlagId:
            del record
        return jsonify({
            "status": 200,
            "data":[{
                "id":  record.incidentId,
                "message": "red-flag record has been deleted"}]
        }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200
