# """ review status codes"""
from flask import Blueprint, jsonify, request, Response, json
from models.incident_model import Intervention,intervention_table

# from api.views.auth_helper import token_required,non_admin_required,admin_required

intervention_bp = Blueprint('intervention_bp', __name__, url_prefix='/api/v1')



@intervention_bp.route('/intervention', methods=['GET'])
def get_all_intervention():
    """docstring function that return all redflags detials"""
    intervention_list = []
    for record in intervention_table:
        if record.type == "intervention":
            intervention_list.append(record.get_incident_details())

    return jsonify({
        "status": 200,
        "data": intervention_list
    }), 200


@intervention_bp.route('/intervention/<int:intervention_Id>', methods=['GET'])
def get_specific_intervention(intervention_Id):
    for record in intervention_table:
        if record.incidentId == intervention_Id:
            return jsonify({
                "status": 200,
                "data": record.get_incident_details()
            }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@intervention_bp.route('/intervention', methods=['POST'])
def create_intervention():
    data = request.get_json()
    if data:
        try:
            location = {"locationLong": data["locationLong"], "locationLat": data["locationLat"]}
            newIncident = Intervention(location=location, createdBy=data['createdBy'], \
                                       images=data['images'], videos=data['videos'], \
                                       comment=data['comment'])
        except KeyError:
            return jsonify({"Required format": {
                "comment": "Intervention comment",
                "createdBy": 2,
                "images": "image name",
                "locationLong": "0.0000",
                "locationLat": "0.00000",
                "videos": "video name"
            }}), 400

        intervention_table.append(newIncident)
        return jsonify({
            "status": 200,
            "data": [{
                "id": intervention_table[-1].incidentId,
                "message": "Created intervention record"}]
        }), 200


@intervention_bp.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
def update_intervention_location(intervention_Id):
    for incident in intervention_table:
        if incident.incidentId == intervention_Id:
            data = request.get_json()
            location = {"locationLong": data['locationLong'], "locationLat": data['locationLat']}
            incident.set_location(location)
            return jsonify({
                "status": 200,
                "data": [{
                    "id": incident.incidentId,
                    "message": "Updated intervention record's location"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@intervention_bp.route('/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
def update_intervention_comment(intervention_Id):
    for incident in intervention_table:
        if incident.incidentId == intervention_Id:
            data = request.get_json()
            comment = data['comment']
            incident.set_comment(comment)
            return jsonify({
                "status": 200,
                "data": [{
                    "id": incident.get_incident_details(),
                    "message": "Updated intervention record's comment"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@intervention_bp.route('/intervention/<int:intervention_Id>', methods=['DELETE'])
def delete_intervention(intervention_Id):
    for incident in intervention_table:
        if incident.incidentId == intervention_Id:
            incident_index = intervention_table.index(incident)
            intervention_table.pop(incident_index)
            del incident
            return jsonify({"status": 200, "data": [{"id": intervention_Id,
                                                     "message": "intervention record has been deleted"}]}), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200
