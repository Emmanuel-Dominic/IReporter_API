from flask import Blueprint, jsonify, request
from api.helpers.auth import token_required, admin_required, non_admin_required, get_current_user
from api.controllers.incident_controller import mailme, get_incidents_by_status, get_incidents_by_type, \
    get_incidents_by_id, create_incident, update_incident_comment, update_incident_location, update_incident_status, \
    delete_incident
from api.helpers.validators import verify_create_incident_data, bad_request, not_found
from api.models.database_model import DatabaseConnection

db = DatabaseConnection

intervention_bp = Blueprint('intervention_bp', __name__, url_prefix='/api/v1')


@intervention_bp.route('/intervention', methods=['POST'])
@token_required
@non_admin_required
@verify_create_incident_data
def create_intervention():
    incident = create_incident()
    if incident:
        return jsonify({"status": 201, "data": [incident,
                                                {"message": "Intervention Successfully created"}]}), 201
    return bad_request()


@intervention_bp.route('/intervention', methods=['GET'])
@token_required
def get_intervention():
    intervention = get_incidents_by_type('intervention')
    if intervention:
        return jsonify({"status": 200, "data": intervention}), 200
    return not_found()


@intervention_bp.route('/intervention/<int:intervention_Id>', methods=['GET'])
@token_required
def get_specific_intervention(intervention_Id):
    intervention = get_incidents_by_id(int(intervention_Id))
    if intervention:
        return jsonify({"status": 200, "data": intervention}), 200
    return not_found()


@intervention_bp.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_location(intervention_Id):
    can_not_edit = get_incidents_by_status(int(intervention_Id))
    incident = update_incident_location(int(intervention_Id))
    if can_not_edit:
        return can_not_edit
    elif incident:
        return jsonify({"status": 200, "Data": [incident,
                                                {"message": "Intervention location successfully Updated"}]}), 200
    return bad_request()


@intervention_bp.route('/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_comment(intervention_Id):
    can_not_edit = get_incidents_by_status(int(intervention_Id))
    incident = update_incident_comment(int(intervention_Id))
    if can_not_edit:
        return can_not_edit
    elif incident:
        return jsonify({"status": 200, "Data": [incident,
                                                {"message": "Intervention comment successfully Updated"}]}), 200
    return bad_request()


@intervention_bp.route('/intervention/<int:intervention_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_intervention(intervention_Id):
    incident = get_incidents_by_id(int(intervention_Id))
    delete = delete_incident(intervention_Id,'intervention')
    if not incident:
        return not_found()
    elif delete:
        return jsonify({"status": 200, "Data": [delete,
                                                {"message": "Intervention successfully Deleted"}]}), 200
    return bad_request()


@intervention_bp.route('/intervention/<int:intervention_Id>/status', methods=['PATCH'])
@token_required
@admin_required
def update_intervention_status(intervention_Id):
    incident = get_incidents_by_id(int(intervention_Id))
    incident_status = update_incident_status(int(intervention_Id))
    if not incident:
        return not_found()
    elif incident_status:
        mail = mailme(int(incident_status["incident_id"]))
        return jsonify({"status": 200, "Data": [incident_status,
                                                {"message": "Intervention status successfully Updated"},
                                                {"Email": mail}]}), 200
    return bad_request()
