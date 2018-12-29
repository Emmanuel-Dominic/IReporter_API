from flask import Blueprint, jsonify, request, json
from api.helpers.auth import token_required, admin_required, non_admin_required,get_current_user
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



@incident_bp.route('/auth/intervention', methods=['GET'])
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


@incident_bp.route('/auth/red-flags', methods=['GET'])
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



@incident_bp.route('/auth/intervention/<int:intervention_Id>', methods=['GET'])
@token_required
@non_admin_required
def get_specific_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    return jsonify({"data":[intervention.get_incident_details()]},{
        "status": 200}), 200


@incident_bp.route('/auth/red-flag/<int:redflag_Id>', methods=['GET'])
@token_required
@non_admin_required
def get_specific_redflag(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    return jsonify({"data":[red_flag.get_incident_details()]},{
        "status": 200}), 200


@incident_bp.route('/auth/intervention/<int:intervention_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_location(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention.status == "draft": 
        data = request.get_json()
        locationLong_value = data['locationLong']
        locationLat_value = data['locationLat']
        intervention.locationLong=locationLong_value
        intervention.locationLat=locationLat_value
        return jsonify({
            "status": 200},
            {"data": intervention.incidentId},
            {"message": "Updated intervention record's location"}), 200
    return jsonify({"message":"Sorry, intervention location update not possible"}),406


@incident_bp.route('/auth/red-flag/<int:redflag_Id>/location', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_location(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if red_flag.status == "draft":
        data = request.get_json()
        locationLong_value = data['locationLong']
        locationLat_value = data['locationLat']
        red_flag.locationLong=locationLong_value
        red_flag.locationLat=locationLat_value
        return jsonify({
            "status": 200},
            {"data": red_flag.incidentId},
            {"message": "Updated intervention record's location"}), 200
    return jsonify({"message":"Sorry, redflag location update not possible"}),406

@incident_bp.route('/auth/intervention/<int:intervention_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_intervention_comment(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention.status == "draft": 
        data = request.get_json()
        comment_value = data['comment']
        intervention.comment=comment_value
        return jsonify({
            "status": 200},
            {"data": intervention.incidentId,
            "message": "Updated intervention record's comment"
        }), 200
    return jsonify({"message":"Sorry, intervention comment update not possible"}),406


@incident_bp.route('/auth/red-flag/<int:redflag_Id>/comment', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_comment(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if intervention.status == "draft": 
        data = request.get_json()
        comment_value = data['comment']
        red_flag.comment = comment_value
        return jsonify({
            "status": 200,
            "data": [{
                "id": red_flag.incidentId,
                "message": "Updated intervention record's comment"}]
        }), 200
    return jsonify({"message":"Sorry, redflag comment update not possible"}),406


@incident_bp.route('/auth/intervention/<int:intervention_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_intervention(intervention_Id):
    intervention=get_incidents_by_type_id("intervention",intervention_Id)
    if intervention:
        incident_index = intervention_table.index(intervention)
        intervention_table.pop(incident_index)
        del intervention
        return jsonify({"status": 200}, 
            {"data": [{"id": intervention_Id},
            {"message": "intervention record has been deleted"}]}), 200
    return jsonify({"message":"intervention of Id {} is not found please".format(intervention_Id)})


@incident_bp.route('/auth/red-flag/<int:redflag_Id>', methods=['DELETE'])
@token_required
@non_admin_required
def delete_redflag(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if red_flag:
        incident_index = redflag_table.index(red_flag)
        redflag_table.pop(incident_index)
        del red_flag
        return jsonify({"status": 200}, 
            {"data": [{"id": redflag_Id},
            {"message": "redflag record has been deleted"}]}), 200
    return jsonify({"message":"redflag of Id {} is not found please".format(redflag_Id)})



@incident_bp.route('/auth/intervention/<int:intervention_Id>/status', methods=['PATCH'])
@token_required
@non_admin_required
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
                "message": "Updated intervention record's status"}]
        }), 200
    return jsonify({"error":"Sorry, Bad request"}),400
 


@incident_bp.route('/auth/red-flag/<int:redflag_Id>/status', methods=['PATCH'])
@token_required
@non_admin_required
def update_redflag_status(redflag_Id):
    red_flag=get_incidents_by_type_id("redflag",redflag_Id)
    if red_flag:
        data = request.get_json()
        status_value = data['status']
        red_flag.status=status_value
        return jsonify({
            "status": 200},
            {"data":[ {"id":red_flag.incidentId},
            {"message": "Updated intervention record's status"}]}
        ), 200
    return jsonify({"error":"Sorry, Bad request"}),400



@incident_bp.route('/auth/intervention', methods=['POST'])
@token_required
@non_admin_required
def create_intervention():
    data = request.get_json()
    if data:
        try:
            newIncident = Intervention(locationLong=data["locationLong"], \
                            locationLat=data["locationLat"], createdBy=get_current_user()["userId"], \
                            images=data['images'], videos=data['videos'], comment=data['comment'])
        except KeyError:
            return jsonify({"Required format": {
                "comment": "Intervention comment",
                "createdBy": 2,
                "images": "image name",
                "locationLong": 0.0576,
                "locationLat": 0.001516,
                "videos": "video name"
            }}), 400

        intervention_table.append(newIncident)
        return jsonify({
            "status": 200,
            "data": [{
                "id": intervention_table[-1].get_incident_details(),
                "message": "Created intervention record"}]
        }), 200
    return jsonify({"status": 400,
                "message": "Bad request"
                }), 400


@incident_bp.route('/auth/red-flags', methods=['POST'])
@token_required
@non_admin_required
def create_redflag():
    data = request.get_json()
    if data:
        try:
            newIncident = RedFlag(locationLong=data["locationLong"], locationLat=data["locationLat"], createdBy=get_current_user()["userId"], \
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

        redflag_table.append(newIncident)
        return jsonify({
            "status": 200,
            "data": [{
                "id": redflag_table[-1].get_incident_details(),
                "message": "Created redflag record"}]
        }), 200



if __name__ == '__main__':
    app.run(debug=True)


# incident_bp.route('/userId/intervention', methods=['GET'])
# def get_all_intervention_user(userId):
#     intervention_table = []
#     intervention=get_incidents_by_type_by_given_user("intervention",userId)
#     intervention_table.append(intervention)
#     return intervention_table
