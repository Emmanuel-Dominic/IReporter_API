from flask import Blueprint, jsonify, request, json
from api.helpers.auth import token_required, admin_required, non_admin_required,get_current_user
from api.models.incident_model import Intervention, intervention_table,RedFlag,redflag_table,Incident
from api.helpers.incidenthelper import get_incidents_by_type,get_incidents_by_type_id,get_incidents_by_status
from api.helpers.validators import verify_create_incident_data

incident_bp = Blueprint('incident_bp', __name__, url_prefix='/api/v1')


@incident_bp.route("/")
def index():
    return jsonify({
                "IReporter": "This enables any/every citizen to bring"
                " any form of corruption to the notice of appropriate"
                " authorities and the general public."}),200

@incident_bp.route('/intervention', methods=['GET'])
@token_required
def get_all_intervention():
    intervention=get_incidents_by_type("intervention")
    if intervention:
        return jsonify({
                    "status": 200,
                    "data": intervention
                }), 200

@incident_bp.route('/red-flags', methods=['GET'])
@token_required
def get_all_redflag():
    redflag=get_incidents_by_type("redflag")
    return jsonify({
                "status": 200,
                "data": redflag
            }), 200

@incident_bp.route('/intervention/<int:intervention_Id>', methods=['GET'])
@token_required
def get_specific_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention:
        return jsonify({"data":intervention.get_incident_details(),
            "status": 200}), 200
    return not_found() 

@incident_bp.route('/red-flags/<int:redflag_Id>', methods=['GET'])
@token_required
def get_specific_redflag(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if red_flag:            
        return jsonify({"data":red_flag.get_incident_details()},{
            "status": 200}), 200
    return not_found() 

@incident_bp.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
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

@incident_bp.route('/red-flags/<int:redflag_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_location(redflag_Id):
    incident_obj= get_incidents_by_type_id("redflag",redflag_Id)
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
            "data": {"id":incident_obj.incidentId,
            "message": "Updated redflag record's location"}}), 200

@incident_bp.route('/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
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

@incident_bp.route('/red-flags/<int:redflag_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_comment(redflag_Id):
    incident_obj=get_incidents_by_type_id("redflag",redflag_Id)
    can_not_edit=get_incidents_by_status(incident_obj)
    if can_not_edit:
        return can_not_edit
    else:
        data = request.get_json()
        comment_value = data['comment']
        incident_obj.comment = comment_value
        return jsonify({
            "status": 200,
            "data": [{
                "id": incident_obj.incidentId,
                "message": "Updated redflag record's comment"}]
        }), 200

@incident_bp.route('/intervention/<int:intervention_Id>', methods=['DELETE'])
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

@incident_bp.route('/red-flags/<int:redflag_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_redflag(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if red_flag:
        incident_index = redflag_table.index(red_flag)
        redflag_table.pop(incident_index)
        del red_flag
        return jsonify({"status": 200, 
            "data": {"id": redflag_Id,
            "message": "redflag record has been deleted"}}), 200
    return not_found()

@incident_bp.route('/intervention/<int:intervention_Id>/status', methods=['PATCH'])
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

@incident_bp.route('/red-flags/<int:redflag_Id>/status', methods=['PATCH'])
@token_required
@admin_required
def update_redflag_status(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if red_flag:
        data = request.get_json()
        status_value = data['status']
        red_flag.status=status_value
        return jsonify({
            "status": 200,
            "data": {"id":red_flag.incidentId,
            "message": "Updated redflag record's status"}}), 200
    return not_found()

@incident_bp.route('/intervention', methods=['POST'])
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

@incident_bp.route('/red-flags', methods=['POST'])
@token_required
@non_admin_required
@verify_create_incident_data
def create_redflag():
    data = request.get_json()
    if data:
        newIncident = RedFlag(locationLong=data["locationLong"], locationLat=data["locationLat"], createdBy=get_current_user()["userId"], \
                                   images=data['images'], videos=data['videos'], \
                                   comment=data['comment'])
        redflag_table.append(newIncident)
        return jsonify({
            "status": 201,
            "data": [{
                "id": redflag_table[-1].incidentId,
                "message": "Created redflag record"}]
        }), 201

# def bad_request():
#     return jsonify({"status":400, "error": "Sorry, Bad request"}),400

def not_found():
    return jsonify({"status":404, "error": "Sorry, Incident Not Found"}),404

