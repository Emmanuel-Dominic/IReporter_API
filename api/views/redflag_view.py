from flask import Blueprint, jsonify, request
from api.helpers.auth import token_required, non_admin_required, admin_required,get_current_user
from api.models.incident_model import RedFlag, redflag_table

redflag_bp = Blueprint('redflag_bp', __name__, url_prefix='/api/v1')

@redflag_bp.route('/')
def index():
    return jsonify({
        'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}), 200

@redflag_bp.route('/red-flags', methods=['GET'])
@token_required
@non_admin_required
def get_all_redflags():
    """docstring function that return all redflags detials"""
    redflags_list = []
    for record in redflag_table:
        if record.type == "red-flag":
            redflags_list.append(record.get_incident_details())
    return jsonify({
        "status": 200,
        "data": redflags_list
    }), 200


@redflag_bp.route('/red-flags/<int:redflag_Id>', methods=['GET'])
@token_required
@non_admin_required
def get_specific_redflag(redflag_Id):
    for record in redflag_table:
        if record.incidentId == redflag_Id:
            return jsonify({
                "status": 200,
                "data": record.get_incident_details()
            }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@redflag_bp.route('/red-flags', methods=['POST'])
@token_required
@non_admin_required
def create_redflag():
    data = request.get_json()
    if data:
        try:
            newIncident = RedFlag(locationLong=data["locationLong"], locationLat=data["locationLat"], \
                                        comment=data['comment'],createdBy=get_current_user(), \
                                       images=data['images'], videos=data['videos'])
        except KeyError:
            return jsonify({"Required format": {
                "comment": "Redflag comment",
                "images": "image name",
                "locationLong": 0.0000,
                "locationLat": 0.00000,
                "videos": "video name"
            }}), 400
        redflag_table.append(newIncident)
        return jsonify({
            "status": 200,
            "data": [{
                "id": redflag_table[-1].incidentId,
                "message": "Created red-flag record"}]
        }), 201


@redflag_bp.route('/red-flags/<int:redflag_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_location(redflag_Id):
    for incident in redflag_table:
        if incident.incidentId == redflag_Id:
            data = request.get_json()
            locationLong= data['locationLong']
            locationLat= data['locationLat']

            incident.set_locationLong(locationLong)
            incident.set_locationLat(locationLat)
            return jsonify({
                "status": 200,
                "data": [{
                    "id": incident.incidentId,
                    "message": "Updated red-flag record's location"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@redflag_bp.route('/red-flags/<int:redflag_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_comment(redflag_Id):
    for incident in redflag_table:
        if incident.incidentId == redflag_Id:
            data = request.get_json()
            comment = data['comment']
            incident.set_comment(comment)
            return jsonify({
                "status": 200,
                "data": [{
                    "id": incident.incidentId,
                    "message": "Updated red-flag record's comment"}]
            }), 200

    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200


@redflag_bp.route('/red-flags/<int:redflag_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_redflag(redflag_Id):
    for incident in redflag_table:
        if incident.incidentId != redflag_Id:
            incident_index = redflag_table.index(incident)
            redflag_table.pop(incident_index)
            del incident
            return jsonify({"status": 200, "data": [{"id": redflag_Id,
                                                     "message": "red-flag record has been deleted"}]}), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200

@redflag_bp.route('/red-flags/<int:redflag_Id>/status', methods=['PATCH'])
@token_required
@admin_required
def update_redflag_status(redflag_Id):
    for incident in redflag_table:
        if incident.incidentId == redflag_Id:
            data = request.get_json()
            status = data['status']
            incident.set_status(status)
            return jsonify({
                "status": 200,
                "data": [{
                    "id": incident.incidentId,
                    "message": "Updated red-flag record's status"}]
            }), 200
    return jsonify({
        "status": 404,
        "error": "bad request"
    }), 200
