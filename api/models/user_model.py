import datetime

class User:
    """docstring for User."""

    userId = 1

    def __init__(self, userName, name, email, phoneNumber, password):
        self.firstName = name['firstName']
        self.lastName = name['lastName']
        self.otherName = name['otherName']
        self.email = email
        self.phoneNumber = phoneNumber
        self.password = password
        self.userName = userName
        self.date = datetime.datetime.now()
        self.userId = User.userId
        self.isAdmin = False
        User.userId += 1

    def get_name(self):
        return "".join([self.firstName, self.lastName, self.otherName])

    def get_user_details(self):
        return {
            "name":self.get_name(),
            "userName":self.userName,
            "email":self.email,
            "phoneNumber":self.phoneNumber,
            "isAdmin":self.isAdmin,
            "userId":self.userId
            }
