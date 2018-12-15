from flask import jsonify, json
import re
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """docstring for User."""

    userId = 1

    def __init__(self, userName, name, email, phoneNumber, password):
        self.firstName = self.set_firstName(name["firstName"])
        self.lastName = self.set_lastName(name["lastName"])
        self.otherName = self.set_otherName(name["otherName"])
        self.name = name
        self.email = self.set_email(email)
        self.phoneNumber = self.set_phoneNumber(phoneNumber)
        # self.password = generate_password_hash(password)
        self.password = self.set_password(password)
        self.userName = self.set_userName(userName)
        self.date = datetime.datetime.now()
        self.userId = User.userId
        self.isAdmin = False
        User.userId += 1

    def set_password(self,password):
        return generate_password_hash(password)

    def check_password(self, password):
            return check_password_hash(self.password, password)

    def set_email(self,email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return jsonify({"message":"Your email address is not valid."}), 406
        return email


    def set_userName(self,userName):
        if not isinstance(userName,str):
            return jsonify({"error":"Invalid, userName must be a string"}), 406
        return userName


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


    def set_phoneNumber(self,phoneNumber):
        if not isinstance(phoneNumber,int):
            return jsonify({"error":"Invalid, must be a phone number"}), 406
        return phoneNumber


    def get_name(self):
        return " ".join([self.name["firstName"], self.name["lastName"], self.name["otherName"]])


    def get_user_details(self):
        data = {"name":self.get_name(), "userName": self.userName, \
            "email": self.email, "phoneNumber": self.phoneNumber, \
            "isAdmin": self.isAdmin, "userId": self.userId}
        return data

users_table = []

if __name__ == '__main__':
    admin_user =User(
        name={"firstName": "Admin", "lastName": "AdminLastname", \
              "otherName": "Othername"},
        userName="admin",
        email="admin@ireporter.com",
        phoneNumber=256700701616,
        password="admin123"
    )
    admin_user.isAdmin = True
    users_table.append(admin_user)
