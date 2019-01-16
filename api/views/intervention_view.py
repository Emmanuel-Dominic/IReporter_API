from flask import Blueprint, jsonify, request
from api.helpers.auth import token_required, admin_required, non_admin_required,get_current_user
from api.models.incident_model import Intervention, intervention_table,RedFlag,redflag_table
from api.helpers.incidenthelper import not_found,get_incidents_by_type,get_incidents_by_type_id,get_incidents_by_status
from api.helpers.validators import verify_create_incident_data

intervention_bp = Blueprint('intervention_bp', __name__, url_prefix='/api/v1')


@intervention_bp.route('/intervention', methods=['POST'])
@token_required
@non_admin_required
@verify_create_incident_data
def create_intervention():
    data = request.get_json()
    if data:
        newIncident = Intervention(locationLong=data["locationLong"], \
                        locationLat=data["locationLat"], createdBy=get_current_user()["userId"], \
                        images=data['images'], videos=data['videos'], comment=data['comment'])
        intervention_table.append(newIncident)
        return jsonify({
            "status": 201,
            "data": [{
                "id": intervention_table[-1].incidentId,
                "message": "Created intervention record"}]
        }), 201



@intervention_bp.route('/intervention', methods=['GET'])
@token_required
def get_all_intervention():
    intervention=get_incidents_by_type("intervention")
    if intervention:
        return jsonify({
                    "status": 200,
                    "data": intervention
                }), 200


@intervention_bp.route('/intervention/<int:intervention_Id>', methods=['GET'])
@token_required
def get_specific_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention:
        return jsonify({"data":intervention.get_incident_details(),
            "status": 200}), 200
    return not_found() 


@intervention_bp.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_location(intervention_Id):
    incident_obj=get_incidents_by_type_id("intervention",int(intervention_Id))
    can_not_edit=get_incidents_by_status(incident_obj)
    if can_not_edit:
        return can_not_edit
    else:
        data = request.get_json()
        locationLong_value = data['locationLong']
        locationLat_value = data['locationLat']
        incident_obj.locationLong=locationLong_value
        incident_obj.locationLat=locationLat_value
        return jsonify({
            "status": 200,
            "data":{"id": incident_obj.incidentId, "message": "Updated intervention record's location"}}), 200


@intervention_bp.route('/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_comment(intervention_Id):
    incident_obj=get_incidents_by_type_id("intervention",intervention_Id)
    can_not_edit=get_incidents_by_status(incident_obj)
    if can_not_edit:
        return can_not_edit
    else:
        data = request.get_json()
        comment_value = data['comment']
        incident_obj.comment=comment_value
        return jsonify({
            "status": 200,
            "data": {"id":incident_obj.incidentId,
            "message": "Updated intervention record's comment"}
        }), 200


@intervention_bp.route('/intervention/<int:intervention_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention:
        incident_index = intervention_table.index(intervention)
        intervention_table.pop(incident_index)
        del intervention
        return jsonify({"status": 200,
            "data": {"id": intervention_Id,
            "message": "intervention record has been deleted"}}), 200
    return not_found()


@intervention_bp.route('/intervention/<int:intervention_Id>/status', methods=['PATCH'])
@token_required
@admin_required
def update_intervention_status(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention:
        data = request.get_json()
        status_value = data['status']
        intervention.status=status_value
        return jsonify({
            "status": 200,
            "data": [{
                "id": intervention.incidentId,
                "message": "Updated intervention record's status"}]}), 200
    return not_found()

