from flask import Blueprint, jsonify, request, json
from api.helpers.auth import token_required, admin_required, non_admin_required
from api.models.incident_model import Intervention, intervention_table,RedFlag,redflag_table
from api.helpers.incidenthelper import get_incidents_by_type,get_incidents_by_type_id
# ,get_incidents_by_type_by_given_user

incident_bp = Blueprint('incident_bp', __name__, url_prefix='/api/v1')



@incident_bp.route("/")
def index():
    return jsonify({
                "IReporter": "This enables any/every citizen to bring"
                " any form of corruption to the notice of appropriate"
                " authorities and the general public."}),200



@incident_bp.route('/intervention', methods=['GET'])
@token_required
@non_admin_required
def get_all_intervention():
    intervention_list = []
    intervention=get_incidents_by_type("intervention")
    intervention_list.append(intervention)
    return jsonify({
                "status": 200,
                "data": intervention_list
            }), 200


@incident_bp.route('/red-flags', methods=['GET'])
@token_required
@non_admin_required
def get_all_redflag():
    redflag_list = []
    redflag=get_incidents_by_type("redflag")
    redflag_list.append(redflag)
    return jsonify({
                "status": 200,
                "data": redflag_list
            }), 200



@incident_bp.route('/intervention/<int:intervention_Id>', methods=['GET'])
@token_required
@non_admin_required
def get_specific_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    return jsonify({"data":[intervention]},{
        "status": 200}), 200


@incident_bp.route('/red-flags/<int:redflag_Id>', methods=['GET'])
@token_required
@non_admin_required
def get_specific_redflag(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    return jsonify({"data":[red_flag]},{
        "status": 200}), 200


@incident_bp.route('/intervention/<int:intervention_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_location(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    data = request.get_json()
    locationLong= data['locationLong']
    locationLat= data['locationLat']
    incidents.set_location(location)
    return jsonify({
        "status": 200},
        {"data": [incident.incidentId]},
        {"message": "Updated intervention record's location"}), 200


@incident_bp.route('/red-flag/<int:redflag_Id>', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_location(intervention_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    data = request.get_json()
    location = {"locationLong": data['locationLong'], "locationLat": data['locationLat']}
    incidents.set_location(location)
    return jsonify({
        "status": 200},
        {"data": [incidents]},
        {"message": "Updated intervention record's location"}), 200

@incident_bp.route('/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_comment(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    data = request.get_json()
    comment = data['comment']
    incidents.set_comment(comment)
    return jsonify({
        "status": 200},
        {"data": [incidents],
        "message": "Updated intervention record's comment"
    }), 200


@incident_bp.route('/red-flag/<int:redflag_Id>', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_comment(intervention_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    data = request.get_json()
    comment = data['comment']
    incident.set_comment(comment)
    return jsonify({
        "status": 200,
        "data": [{
            "id": incident.get_incident_details(),
            "message": "Updated intervention record's comment"}]
    }), 200


@incident_bp.route('/intervention/<int:intervention_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    incident_index = intervention_table.index(incident)
    intervention_table.pop(incident_index)
    del incidents
    return jsonify({"status": 200}, 
        {"data": [{"id": intervention_Id},
        {"message": "intervention record has been deleted"}]}), 200


@incident_bp.route('/red-flag/<int:redflag_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_redflag(intervention_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    incident_index = intervention_table.index(incidents)
    intervention_table.pop(incident_index)
    del incidents
    return jsonify({"status": 200}, 
        {"data": [{"id": intervention_Id},
        {"message": "intervention record has been deleted"}]}), 200


@incident_bp.route('/intervention/<int:intervention_Id>/status', methods=['PATCH'])
@token_required
@admin_required
def update_intervention_status(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    data = request.get_json()
    comment = data['status']
    incidents.set_status(status)
    return jsonify({
        "status": 200,
        "data": [{
            "id": incident.get_incident_details(),
            "message": "Updated intervention record's status"}]
    }), 200


@incident_bp.route('/red-flag/<int:redflag_Id>', methods=['PATCH'])
@token_required
@admin_required
def update_redflag_status(intervention_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    data = request.get_json()
    comment = data['status']
    incident.set_status(status)
    return jsonify({
        "status": 200},
        {"data": [incident.get_incident_details()]},
        {"message": "Updated intervention record's status"}
    ), 200



@incident_bp.route('/intervention', methods=['POST'])
@token_required
@non_admin_required
def create_intervention():
    data = request.get_json()
    if data:
        try:
            newIncident = Intervention(locationLong=data["locationLong"], locationLat=data["locationLat"], createdBy=data['createdBy'], \
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



@incident_bp.route('/red-flags', methods=['POST'])
@token_required
@non_admin_required
def create_redflag():
    data = request.get_json()
    if data:
        try:
            newIncident = RedFlag(locationLong=data["locationLong"], locationLat=data["locationLat"], createdBy=data['createdBy'], \
                                       images=data['images'], videos=data['videos'], \
                                       comment=data['comment'])
        except KeyError:
            return jsonify({"Required format": {
                "comment": "RedFlag comment",
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



if __name__ == '__main__':
    app.run(debug=True)


# incident_bp.route('/userId/intervention', methods=['GET'])
# def get_all_intervention_user(userId):
#     intervention_table = []
#     intervention=get_incidents_by_type_by_given_user("intervention",userId)
#     intervention_table.append(intervention)
#     return intervention_table
