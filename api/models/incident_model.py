from flask import jsonify
import datetime
# from api.views.user_view import


class Incident:
    """docstring for Incident."""


    def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
        self.createdOn = datetime.datetime.today()
        self.locationLong = locationLong
        self.locationLat = locationLat
        self.createdBy = createdBy
        self.comment = comment
        self.images = images
        self.videos = videos
        self.status = "draft"


    def get_incident_details(self):
        return {
            "locationLong": self.locationLong,
            "locationLat": self.locationLat,
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

    redFlag_Id = 1

    def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
        Incident.__init__(self, createdBy, locationLong, locationLat, comment, images, videos)
        self.type = 'red-flag'
        self.incidentId = RedFlag.redFlag_Id
        RedFlag.redFlag_Id += 1


class Intervention(Incident):

    intervention_Id = 1

    def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
        Incident.__init__(self, createdBy, locationLong, locationLat, comment, images, videos)
        self.type = 'intervention'
        self.incidentId = Intervention.intervention_Id
        Intervention.intervention_Id += 1


intervention_table = [
    Intervention(
        comment="Mbale highway needs construction",
        createdBy=2,
        images="1.jpeg",
        locationLong= 0.33737,
        locationLat= 5.38974,
        videos="1.gif"
    ),
    Intervention(
        comment="Mbarara highway needs construction",
        createdBy=2,
        images="1.jpeg",
        locationLong= 0.33737,
        locationLat= 5.38974,
        videos="1.gif"
    )]
intervention_table[0].createdOn = "Fri, 30 Nov 2018 13:09:32 GMT"
intervention_table[1].createdOn = "Fri, 30 Nov 2018 12:09:32 GMT"


redflag_table = [
    RedFlag(
        comment="Arnold was caught stealing jack fruit in hassan's Garden",
        createdBy=2,
        images="1.jpeg",
        locationLong= 0.33737, 
        locationLat= 5.38974,
        videos="1.gif"
    ),
    RedFlag(
        comment="james was caught idle and disorderly",
        createdBy=2,
        images="1.jpeg",
        locationLong= 0.33737, 
        locationLat= 5.38974,
        videos="1.gif"
    )]
redflag_table[0].createdOn = "Fri, 30 Nov 2018 13:09:32 GMT"
redflag_table[1].createdOn = "Fri, 30 Nov 2018 12:09:32 GMT"
