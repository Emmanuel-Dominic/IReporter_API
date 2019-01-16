import datetime

class Incident:
    """docstring for Incident."""


    # def __init__(self, createdBy, locationLong, locationLat, comment, images, videos):
    def __init__(self, **kwargs):
        self.createdOn = datetime.datetime.today()
        self.locationLong = kwargs["locationLong"]
        self.locationLat = kwargs["locationLat"]
        self.createdBy = kwargs["createdBy"]
        self.comment = kwargs["comment"]
        self.images = kwargs["images"]
        self.videos = kwargs["videos"]
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

    def __init__(self, **kwargs):
        Incident.__init__(self, **kwargs)
        self.type = 'red-flag'
        self.incidentId = RedFlag.redFlag_Id
        RedFlag.redFlag_Id += 1


class Intervention(Incident):

    intervention_Id = 1

    def __init__(self, **kwargs):
        Incident.__init__(self, **kwargs)
        self.type = 'intervention'
        self.incidentId = Intervention.intervention_Id
        Intervention.intervention_Id += 1


intervention_table = [ ]

redflag_table = [ ]
