from flask import jsonify
from api.models.incident_model import intervention_table,redflag_table

def get_incidents_by_type_id(incident_type,incId):
    """Check for incident id in users records"""
    incident_table = {"intervention": intervention_table, "redflag": redflag_table }
    for incident in incident_table[incident_type]:
    	if incident.incidentId == incId:
    		return incident
    return None

def get_incidents_by_status(incident_obj):
    """Response to incident status in users records"""
    if not incident_obj:
    	return jsonify({"status":404, "error": "Sorry, Incident Not Found"}),404
    elif incident_obj.status != "draft":
   		return jsonify({"status":406, "error": "Sorry, Update not Possible"}),406


def get_incidents_by_type(incident_type):
    """Check for incident type for agiven record"""
    incident_table = {"intervention": intervention_table, "redflag": redflag_table}
    incidents_list=[]
    for record in incident_table[incident_type]:
    	incidents_list.append(record.get_incident_details())
    return incidents_list


def not_found():
    """Returns not found for agiven record"""
    return jsonify({"status":404, "error": "Sorry, Incident Not Found"}),404
