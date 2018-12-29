from flask import Blueprint, jsonify, request
from api.helpers.auth import (
    token_required,
    non_admin_required,
    admin_required,
    get_current_user,
)
from api.models.incident_model import RedFlag, redflag_table
from api.helpers.incidenthelper import get_incidents_by_type, get_incidents_by_type_id


redflag_bp = Blueprint("redflag_bp", __name__, url_prefix="/api/v1")


@redflag_bp.route("/")
def index():
    return jsonify({
                "IReporter": "This enables any/every citizen to bring"
                " any form of corruption to the notice of appropriate"
                " authorities and the general public."}),200


@redflag_bp.route("/red-flags", methods=["GET"])
@token_required
@non_admin_required
def get_all_redflags():
    """docstring function that return all redflags detials"""
    redflag_list = []
    redflag = get_incidents_by_type("redflag")
    redflag_list.append(redflag)
    return jsonify({"status": 200, "data": redflag_list}), 200


@redflag_bp.route("/red-flags/<int:redflag_Id>", methods=["GET"])
@token_required
@non_admin_required
def get_specific_redflag(redflag_Id):
    red_flag = get_incidents_by_type_id("redflag", redflag_Id)
    if red_flag:
        red = red_flag.get_incident_details()
        return jsonify({"data": [red]}, {"status": 200}),200
    return jsonify({"status": 404, "error": "bad request"}), 404


@redflag_bp.route("/red-flags", methods=["POST"])
@token_required
@non_admin_required
def create_redflag():
    data = request.get_json()
    if data:
        try:
            newIncident = RedFlag(
                locationLong=data["locationLong"],
                locationLat=data["locationLat"],
                createdBy=get_current_user()["userId"],
                images=data["images"],
                videos=data["videos"],
                comment=data["comment"],
            )
        except KeyError:
            return jsonify(
                    {
                        "Required format": {
                            "comment": "Redflag comment",
                            "createdBy": 2,
                            "images": "image name",
                            "locationLong": 0.98498,
                            "locationLat": 0.94996,
                            "videos": "video name",
                        }
                    }),406
        redflag_table.append(newIncident)
        return jsonify({"status": 201,
                    "data": [{"id": redflag_table[-1].incidentId,
                            "message": "Created red-flag record"}]}),201
    return jsonify({"status": 404, "error": "bad request"}), 404


@redflag_bp.route("/red-flags/<int:redflag_Id>/location", methods=["PATCH"])
@token_required
@non_admin_required
def update_redflag_location(redflag_Id):
    red_flag = get_incidents_by_type_id("redflag", redflag_Id)
    if red_flag:
        data = request.get_json()
        locationLong_value = data["locationLong"]
        locationLat_value = data["locationLat"]
        red_flag.locationLong = locationLong_value
        red_flag.locationLat = locationLat_value
        return jsonify({"status": 200,
                    "data": [{"id": red_flag.incidentId,
                            "message": "Updated red-flag record's location"}]}),200
    return jsonify({"status": 404, "error": "bad request"}), 200


@redflag_bp.route("/red-flags/<int:redflag_Id>/comment", methods=["PATCH"])
@token_required
@non_admin_required
def update_redflag_comment(redflag_Id):
    red_flag = get_incidents_by_type_id("redflag", redflag_Id)
    if red_flag:
        data = request.get_json()
        comment_value = data["comment"]
        red_flag.comment = comment_value
        return (jsonify({"status": 200,
                    "data": [{"id": red_flag.incidentId,
                            "message": "Updated intervention record's comment"}]},),200,
        )
    return jsonify({"message": "Sorry, redflag comment update not possible"}), 406


@redflag_bp.route("/red-flags/<int:redflag_Id>", methods=["DELETE"])
@token_required
@non_admin_required
def delete_redflag(redflag_Id):
    red_flag = get_incidents_by_type_id("redflag", redflag_Id)
    if red_flag:
        incident_index = redflag_table.index(red_flag)
        redflag_table.pop(incident_index)
        del red_flag
        return jsonify(
                {"status": 200},
                {"data": [{"id": redflag_Id},
                        {"message": "redflag record has been deleted"}]}),200
    return jsonify({"message": "redflag of Id {} is not found please".format(redflag_Id)})


@redflag_bp.route("/red-flags/<int:redflag_Id>/status", methods=["PATCH"])
@token_required
@admin_required
def update_redflag_status(redflag_Id):
    red_flag = get_incidents_by_type_id("redflag", redflag_Id)
    if red_flag:
        data = request.get_json()
        status_value = data["status"]
        red_flag.status = status_value
        return jsonify(
                {"status": 200},
                {"data": [{"id": red_flag.incidentId},
                        {"message": "Updated intervention record's status"}]}),200
    return jsonify({"error": "Sorry, Bad request"}), 404
