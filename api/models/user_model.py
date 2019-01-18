import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """User class"""
    userId = 1
    def __init__(self, name, **kwargs):
        self.firstName = name["firstName"]
        self.lastName = name["lastName"]
        self.otherName = name["otherName"]
        self.name = name
        self.email = kwargs["email"]
        self.phoneNumber = kwargs["phoneNumber"]
        self.password = generate_password_hash(kwargs["password"])
        self.userName = kwargs["userName"]
        self.date = datetime.datetime.now()
        self.userId = User.userId
        self.isAdmin = False
        User.userId += 1


    def check_password(self, password):
        """check for hashed password"""
        return check_password_hash(self.password, password)


    def get_name(self):
        """Returns joint names"""
        return " ".join([self.name["firstName"], self.name["lastName"], self.name["otherName"]])


    def get_user_details(self):
        """Returns given user details"""
        data = {"name":self.get_name(), "userName": self.userName, \
            "email": self.email, "phoneNumber": self.phoneNumber, \
            "isAdmin": self.isAdmin, "userId": self.userId}
        return data

users_table = []
admin_user =User(
        name={"firstName": "Admin", "lastName": "AdminLastname", \
              "otherName": "Othername"},
        userName="admin",
        email="admin@ireporter.com",
        phoneNumber=256788084708,
        password="admin123"
    )
admin_user.isAdmin = True
users_table.append(admin_user)

