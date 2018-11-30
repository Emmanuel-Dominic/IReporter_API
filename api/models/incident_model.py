import datetime

class Incident:
    """docstring for Incident."""

    incidentId = 1

    def __init__(self, createdBy, location, comment,images,videos):
        self.createdOn = datetime.datetime.today()
        self.createdBy = createdBy
        self.set_location(location)
        self.set_comment(comment)
        self.images = images
        self.videos = videos
        self.status = 'draft'
        self.incidentId = Incident.incidentId
        Incident.incidentId += 1


    def set_location(self,location):
        self.locationLong = location['locationLong']
        self.locationLat = location['locationLat']

    def set_comment(self,comment):
        self.comment = comment


    def get_location(self):
        return " ".join([self.locationLong,',', self.locationLat])


    def get_incident_details(self):
        return {
            "location": self.get_location(),
            "createdOn":self.createdOn,
            "createdBy":self.createdBy,
            "type":self.type,
            "status":self.status,
            "images":self.images,
            "videos":self.videos,
            "comment":self.comment,
            "incidentId":self.incidentId
            }


class Red_flag(Incident):

    def __init__(self, createdBy, location, comment,images,videos):
        Incident.__init__(self, createdBy, location, comment,images,videos)
        self.type = 'red-flag'





class Intervention(Incident):

    def __init__(self, createdBy, location, comment,images,videos):
        Incident.__init__(self, createdBy, location, comment,images,videos)
        self.type = 'intervention'
