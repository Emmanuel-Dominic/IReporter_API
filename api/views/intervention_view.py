from flask import Blueprint, jsonify, request
from api.helpers.auth import token_required, non_admin_required, admin_required, get_current_user
from api.models.incident_model import Intervention, intervention_table
from api.helpers.incidenthelper import get_incidents_by_type, get_incidents_by_type_id


intervention_bp = Blueprint("intervention_bp", __name__, url_prefix="/api/v1")


@intervention_bp.route("/intervention", methods=["GET"])
@token_required
def get_all_intervention():
    """docstring function that return all redflags detials"""
    intervention_list = []
    intervention = get_incidents_by_type("intervention")
    intervention_list.append(intervention)
    return jsonify({"status": 200, "data": intervention_list}), 200


@intervention_bp.route("/intervention/<int:intervention_Id>", methods=["GET"])
@token_required
@non_admin_required
def get_specific_intervention(intervention_Id):
    intervention = get_incidents_by_type_id("intervention", intervention_Id)
    if intervention:
        return jsonify({"status": 200, "data": intervention.get_incident_details()}),200
    return jsonify({"status": 404, "error": "bad request"}), 404


@intervention_bp.route("/intervention", methods=["POST"])
@token_required
@non_admin_required
def create_intervention():
    data = request.get_json()
    if data:
        try:
            newIncident = Intervention(
                locationLong=data["locationLong"],
                locationLat=data["locationLat"],
                images=data["images"],
                videos=data["videos"],
                comment=data["comment"],
                createdBy=get_current_user()["userId"])
        except KeyError:
            return jsonify({
                        "Required format": {
                            "comment": "Intervention comment",
                            "images": "image name",
                            "locationLong": 0.99898,
                            "locationLat": 0.09882,
                            "videos": "video name"}}),400

        intervention_table.append(newIncident)
        return jsonify({
                    "status": 200,
                    "data": [{
                            "id": intervention_table[-1].incidentId,
                            "message": "Created intervention record",
                        }]}),200
    return jsonify({"status": 404, "error": "bad request"}), 404


@intervention_bp.route(
    "/intervention/<int:intervention_Id>/location", methods=["PATCH"]
)
@token_required
@non_admin_required
def update_intervention_location(intervention_Id):
    intervention = get_incidents_by_type_id("intervention", intervention_Id)
    if intervention:
        data = request.get_json()
        locationLong_value = data["locationLong"]
        locationLat_value = data["locationLat"]
        intervention.locationLong = locationLong_value
        intervention.locationLat = locationLat_value
        return (
            jsonify(
                {
                    "status": 200,
                    "data": [
                        {
                            "id": intervention.incidentId,
                            "message": "Updated intervention record's location",
                        }
                    ],
                }
            ),
            200,
        )

    return jsonify({"status": 404, "error": "bad request"}), 200


@intervention_bp.route("/intervention/<int:intervention_Id>/comment", methods=["PATCH"])
@token_required
@non_admin_required
def update_intervention_comment(intervention_Id):
    intervention = get_incidents_by_type_id("intervention", intervention_Id)
    if intervention:
        data = request.get_json()
        comment_value = data["comment"]
        intervention.comment = comment_value
        return (
            jsonify(
                {"status": 200},
                {
                    "data": intervention.incidentId,
                    "message": "Updated intervention record's comment",
                },
            ),
            200,
        )

    return jsonify({"status": 404, "error": "bad request"}), 200


@intervention_bp.route("/intervention/<int:intervention_Id>", methods=["DELETE"])
@token_required
@non_admin_required
def delete_intervention(intervention_Id):
    intervention = get_incidents_by_type_id("intervention", intervention_Id)
    if intervention:
        incident_index = intervention_table.index(intervention)
        intervention_table.pop(incident_index)
        del intervention
        return (
            jsonify(
                {"status": 200},
                {
                    "data": [
                        {"id": intervention_Id},
                        {"message": "intervention record has been deleted"},
                    ]
                },
            ),
            200,
        )
    return jsonify(
        {"message": "intervention of Id {} is not found please".format(intervention_Id)}
    )


@intervention_bp.route("/intervention/<int:intervention_Id>/status", methods=["PATCH"])
@token_required
@admin_required
def update_intervention_status(intervention_Id):
    intervention = get_incidents_by_type_id("intervention", intervention_Id)
    if intervention:
        data = request.get_json()
        status_value = data["status"]
        intervention.status = status_value
        return (
            jsonify(
                {
                    "status": 200,
                    "data": [
                        {
                            "id": intervention.incidentId,
                            "message": "Updated intervention record's status",
                        }
                    ],
                }
            ),
            200,
        )
    return jsonify({"status": 404, "error": "bad request"}), 200
