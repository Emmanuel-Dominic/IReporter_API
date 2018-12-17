import datetime
from api.views.user_view import


class Incident:
    """docstring for Incident."""

    incidentId = 1

    def __init__(self, createdBy, location, comment, images, videos):
        self.createdOn = datetime.datetime.today()
        self.locationLong = self.set_locationLong(location["locationLong"])
        self.locationLat = self.set_locationLat(location["locationLat"])
        self.createdBy = createdBy
        self.location = location
        self.comment = self.set_comment(comment)
        self.images = images
        self.videos = videos
        self.status = 'draft'
        self.incidentId = Incident.incidentId
        Incident.incidentId += 1


    def get_locatiopn(self):
        return " ".join([self.location["locationLong"], self.location["locationLat"]])

    def set_locationLong(self,locationLong):
        if not isinstance(locationLong,int):
            return jsonify({"error":"Invalid, locationLong must be a integer"}), 406
        return locationLong

    def set_locationLat(self,locationLat):
        if not isinstance(locationLat,int):
            return jsonify({"error":"Invalid, locationLat must be a integer"}), 406
        return locationLat

    def set_comment(self,comment):
        if not isinstance(comment,str):
            return jsonify({"error":"Invalid, otherName must be a string"}),406
        return comment

    def set_status(self,status):
        if not isinstance(status,str):
            return jsonify({"error":"Invalid, status must be a string"}), 406
        if status == ""
        return status

    def set_lastName(self,lastName):
        if not isinstance(lastName,str):
            return jsonify({"error":"Invalid, lastName must be a string"}), 406
        return lastName

    def set_otherName(self,otherName):
        if not isinstance(otherName,str):
            return jsonify({"error":"Invalid, otherName must be a string"}),406
        return otherName
    def set_firstName(self,firstName):
        if not isinstance(firstName,str):
            return jsonify({"error":"Invalid, firstName must be a string"}), 406
        return firstName

    def set_lastName(self,lastName):
        if not isinstance(lastName,str):
            return jsonify({"error":"Invalid, lastName must be a string"}), 406
        return lastName

    def set_otherName(self,otherName):
        if not isinstance(otherName,str):
            return jsonify({"error":"Invalid, otherName must be a string"}),406
        return otherName

    def set_location(self, location):
        self.locationLong = location['locationLong']
        self.locationLat = location['locationLat']

    def set_comment(self, comment):
        self.comment = comment

    def set_status(self, status):
        self.comment = status

    def get_location(self):
        return " ".join([self.locationLong, ',', self.locationLat])

    def get_incident_details(self):
        return {
            "location": self.get_location(),
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "type": self.type,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comment": self.comment,
            "incidentId": self.incidentId
        }


class RedFlag(Incident):

    def __init__(self, createdBy, location, comment, images, videos):
        Incident.__init__(self, createdBy, location, comment, images, videos)
        self.type = 'red-flag'


class Intervention(Incident):

    def __init__(self, createdBy, location, comment, images, videos):
        Incident.__init__(self, createdBy, location, comment, images, videos)
        self.type = 'intervention'


def get_incidents_by_type(incident_type):
    incident_table= {
        "intervention":intervention_table,
        "red-flag":redflag_table
    }
    incidents_list = []
    for record in incident_table[incident_type]:
        incidents_list.append(record.get_incident_details())
    return incidents_list


intervention_table = [
    Intervention(
        comment="Mbale highway needs construction",
        createdBy=2,
        images="1.jpeg",
        location={"locationLong": "0.33737", "locationLat": "5.38974"},
        videos="1.gif"
    ),
    Intervention(
        comment="Mbarara highway needs construction",
        createdBy=2,
        images="1.jpeg",
        location={"locationLong": "0.33737", "locationLat": "5.38974"},
        videos="1.gif"
    )]
intervention_table[0].createdOn = "Fri, 30 Nov 2018 13:09:32 GMT"


redflag_table = [
    RedFlag(
        comment="Arnold was caught stealing jack fruit in hassan's Garden",
        createdBy=2,
        images="1.jpeg",
        location={"locationLong": "0.33737", "locationLat": "5.38974"},
        videos="1.gif"
    )]
redflag_table[0].createdOn = "Fri, 30 Nov 2018 13:09:32 GMT"
