"""views file for create, edit, get and delete redflad incidents"""
from flask import Blueprint, jsonify, request, Response, json
from api.models.incident_model import Incident
from api.models.incident_model import RedFlag
from api.models.incident_model import Intervention

incident_bp = Blueprint('incident_bp', __name__, url_prefix='/api/v1')

incidents_db = [
    RedFlag(
    comment = "Arnold was caught stealing jack fruit in hassan's Garden",
    createdBy = 2,
    images = "1.jpeg",
    location={"locationLong":"0.33737", "locationLat":"5.38974"},
    videos = "1.gif"
    )]
incidents_db[0].createdOn = "Fri, 30 Nov 2018 13:09:32 GMT"


@incident_bp.route('/')
def index():
    return jsonify({'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}), 200



@incident_bp.route('/red-flags', methods=['GET'])
def get_all_redflags():
    """docstring function that return all redflags detials"""
    redflags_list = []
    for record in incidents_db:
        if record.type == "red-flag":
            redflags_list.append(record.get_incident_details())

    # if redflags_list:
    return jsonify({
        "status": 200,
        "data": redflags_list
    }), 200

    # if len(redflags_list) == 0:
    #     return jsonify({
    #         "status": 200,
    #         "Message": "No redflags available"
    #     }), 200

    # return jsonify({
    #     "status": 404,
    #     "Error": "Bad request check input values"
    # }), 200



@incident_bp.route('/red-flags/<int:red_Flag_Id>', methods=['GET'])
def get_specific_redflag(red_Flag_Id):
    for record in incidents_db:
        if record.type == 'red-flag' and record.incidentId == red_Flag_Id:
            return jsonify({
                "status": 200,
                "data": record.get_incident_details()
            }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@incident_bp.route('/red-flags', methods=['POST'])
def create_redflag():
    data = request.get_json()
    if data:
        try:
            location = {"locationLong":data["locationLong"], "locationLat":data["locationLat"]}
            newIncident=RedFlag(location=location, createdBy=data['createdBy'],\
                images=data['images'], videos=data['videos'],\
                comment=data['comment'])
        except KeyError:
            return jsonify({"Required format": {
                "comment": "Redflag comment",
                "createdBy": 2,
                "images": "image name",
                "locationLong": "0.0000" ,
                "locationLat":"0.00000",
                "videos": "video name"
                }}),400

        incidents_db.append(newIncident)
        return jsonify({
            "status": 200,
            "data":[{
                "id":incidents_db[-1].incidentId,
                "message": "Created red-flag record"}]
        }), 200




@incident_bp.route('/red-flags/<int:red_Flag_Id>/location', methods=['PATCH'])
def update_redflag_location(red_Flag_Id):
    for incident in incidents_db:
        if incident.type == 'red-flag' and incident.incidentId == red_Flag_Id:
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

@incident_bp.route('/red-flags/<int:red_Flag_Id>/comment', methods=['PATCH'])
def update_redflag_comment(red_Flag_Id):
    for incident in incidents_db:
        if incident.type == 'red-flag' and incident.incidentId == red_Flag_Id:
            data = request.get_json()
            comment = data['comment']
            incident.set_comment(comment)
            return jsonify({
                "status": 200,
                "data":[{
                    "id":  incident.incidentId,
                    "message": "Updated red-flag record's comment"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@incident_bp.route('/red-flags/<int:red_Flag_Id>', methods=['DELETE'])
def delete_redflag(red_Flag_Id):
    for incident in incidents_db:
        if incident.type == 'red-flag' and incident.incidentId == red_Flag_Id:
            incident_index = incidents_db.index(incident)
            incidents_db.pop(incident_index)
            del incident
            return jsonify({"status": 200, "data":[{"id":  red_Flag_Id,
                 "message": "red-flag record has been deleted"}]}), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200



@incident_bp.route('/intervention', methods=['GET'])
def get_all_intervention():
    """docstring function that return all redflags detials"""
    intervention_list = []
    for record in incidents_db:
        if record.type == "intervention":
            intervention_list.append(record.get_incident_details())
    if len(intervention_list) == 0:
        return jsonify({
            "status": 200,
            "data": "No intervention incidence"
        }), 200

    if intervention_list:
        return jsonify({
            "status": 200,
            "data": intervention_list
        }), 200

    # return jsonify({
    #     "status": 404,
    #     "error": "bad request"
    # }), 200



@incident_bp.route('/intervention/<int:intervention_Id>', methods=['GET'])
def get_specific_intervention(intervention_Id):
    for record in incidents_db:
        if record.type == 'intervention' and record.incidentId == intervention_Id:
            return jsonify({
                "status": 200,
                "data": record.get_incident_details()
            }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@incident_bp.route('/intervention', methods=['POST'])
def create_intervention():
    data = request.get_json()
    if data:
        location = {"locationLong":data["locationLong"], "locationLat":data["locationLat"]}
        newIncident=Intervention(location=location, createdBy=data['createdBy'],\
            images=data['images'], videos=data['videos'],\
            comment=data['comment'])
        incidents_db.append(newIncident)
        return jsonify({
            "status": 200,
            "data":[{
                "id":incidents_db[-1].incidentId,
                "message": "Created intervention record"}]
        }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 400


@incident_bp.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
def update_intervention_location(intervention_Id):
    for incident in incidents_db:
        if incident.type == 'intervention' and incident.incidentId == intervention_Id:
            data = request.get_json()
            location = {"locationLong":data['locationLong'], "locationLat":data['locationLat']}
            incident.set_location(location)
            return jsonify({
                "status": 200,
                "data":[{
                    "id":  incident.incidentId,
                    "message": "Updated intervention record's location"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@incident_bp.route('/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
def update_intervention_comment(intervention_Id):
    for incident in incidents_db:
        if incident.type == 'intervention' and incident.incidentId == intervention_Id:
            data = request.get_json()
            comment = data['comment']
            incident.set_comment(comment)
            return jsonify({
                "status": 200,
                "data":[{
                    "id":  incident.get_incident_details(),
                    "message": "Updated intervention record's comment"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@incident_bp.route('/intervention/<int:intervention_Id>', methods=['DELETE'])
def delete_intervention(intervention_Id):
    for incident in incidents_db:
        if incident.type == 'intervention' and incident.incidentId == intervention_Id:
            incident_index = incidents_db.index(incident)
            incidents_db.pop(incident_index)
            del incident
            return jsonify({"status": 200, "data":[{"id":  intervention_Id,
                 "message": "intervention record has been deleted"}]}), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200
