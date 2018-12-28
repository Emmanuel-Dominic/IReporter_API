from api.models.incident_model import intervention_table,redflag_table

def get_incidents_by_type(incident_type):
    incident_table= {
        "intervention":intervention_table,
        "redflag":redflag_table
    }
    incidents_list = []
    for record in incident_table[incident_type]:
        incidents_list.append(record.get_incident_details())
    return incidents_list


def get_incidents_by_type_id(incident_type,incId):
    incident_table= {
        "intervention":intervention_table,
        "redflag":redflag_table
    }
    for record in incident_table[incident_type]:
        if record.incidentId == incId:
            return record


# def get_incidents_by_type_to_admin(incident_type):
#     incident_table= {
#         "intervention":intervention_table,
#         "redflag":redflag_table
#     }
#     incidents_list = []
#     for record in incident_table[incident_type]:
#         incidents_list.append(record.get_incident_details())
#     return incidents_list

# def get_incidents_by_type_by_given_user(incident_type):
#     incident_table= {
#         "intervention":intervention_table,
#         "red-flag":redflag_table
#     }
#     incidents_list = []
#     for record in incident_table[incident_type]:
#         if record["userId"] == createdBy:
#             incidents_list.append(record.get_incident_details())
#         return incidents_list
#     return "False Id user"
