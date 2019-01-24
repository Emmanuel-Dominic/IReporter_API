from flask import Blueprint, jsonify, request
from api.helpers.auth import token_required, admin_required, non_admin_required, get_current_user
from api.controllers.incident_controller import mailme, get_incidents_by_status, get_incidents_by_type, \
    get_incidents_by_id, create_incident, update_incident_comment, update_incident_location, update_incident_status, \
    delete_incident
from api.helpers.validators import verify_create_incident_data, bad_request, not_found
from api.models.database_model import DatabaseConnection

db = DatabaseConnection

redflag_bp = Blueprint('redflag_bp', __name__, url_prefix='/api/v1')


@redflag_bp.route("/")
def index():
    return jsonify({
                       'IReporter': "This enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public."}), 200


@redflag_bp.route('/red-flags', methods=['POST'])
@non_admin_required
@verify_create_incident_data
def create_redflag():
    incident = create_incident()
    if incident:
        return jsonify({"status": 201, "data": [incident,
                                                {"message": "Redflag Successfully created"}]}), 201
    return bad_request()


@redflag_bp.route('/red-flags', methods=['GET'])
@token_required
def get_all_redflags():
    intervention = get_incidents_by_type('redflag')
    if intervention:
        return jsonify({"status": 200, "data": intervention}), 200


@redflag_bp.route('/red-flags/<int:redflag_Id>', methods=['GET'])
@token_required
def get_specific_redflag(redflag_Id):
    intervention = get_incidents_by_id(int(redflag_Id))
    if intervention:
        return jsonify({"status": 200, "data": intervention}), 200
    return not_found()


@redflag_bp.route('/red-flags/<int:redflag_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_location(redflag_Id):
    not_incident_status = get_incidents_by_status(int(redflag_Id))
    incident = update_incident_location(int(redflag_Id))
    if not_incident_status:
        return not_incident_status
    elif incident:
        return jsonify({"status": 200, "Data": [incident,
                                                {"message": "Redflag location successfully Updated"}]}), 200
    return bad_request()


@redflag_bp.route('/red-flags/<int:redflag_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_comment(redflag_Id):
    not_incident_status = get_incidents_by_status(int(redflag_Id))
    incident = update_incident_comment(int(redflag_Id))
    if not_incident_status:
        return not_incident_status
    if incident:
        return jsonify({"status": 200, "Data": [incident,
                                                {"message": "Redflag comment successfully Updated"}]}), 200
    return bad_request()


@redflag_bp.route('/red-flags/<int:redflag_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_redflag(redflag_Id):
    not_found_id = get_incidents_by_id(int(redflag_Id))
    incident = delete_incident(redflag_Id,'redflag')
    if not not_found_id:
        return not_found()
    if incident:
        return jsonify({"status": 200, "Data": [incident,
                                                {"message": "Redflag successfully Deleted"}]}), 200
    return bad_request()


@redflag_bp.route('/red-flags/<int:redflag_Id>/status', methods=['PATCH'])
@token_required
@admin_required
def update_redflag_status(redflag_Id):
    not_incident_id = get_incidents_by_id(int(redflag_Id))
    incident = update_incident_status(int(redflag_Id))
    if not not_incident_id:
        return not_found()
    if incident:
        mail = mailme(int(incident["incident_id"]))
        return jsonify({"status": 200, "Data": [incident,
                                                {"message": "Redflag status successfully Updated"},
                                                {"Email": mail}]}), 200
    return bad_request()
