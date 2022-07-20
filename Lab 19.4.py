import os
import datetime

now = datetime.datetime.now()
print("Programmer:", os.environ['USERPROFILE'])
print('Lab 19.2', now.strftime("%b %d,%Y"), '@', now.strftime("%H:%M:%S"))


class Person:
    def __init__(self, name, address, phoneNum):
        self.name = name
        self.address = address
        self.phoneNum = phoneNum


class Customer(Person):
    def __init__(self, name, address, phoneNum, cusNum, mail):
        Person.__init__(self, name, address, phoneNum)
        self.cusNum = cusNum
        self.mail = mail

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhoneNum(self):
        return self.phoneNum

    def getCusNum(self):
        return self.cusNum

    def getMail(self):
        if self.mail == "No":
            return "False"
        else:
            return "True"


def main():

    devName = input("Enter your name: ")
    name = str(input("Enter the customer's name: "))
    address = str(input("Enter the customer's address: "))
    phoneNum = str(input("Enter the customer's phone number: "))
    cusNum = str(input("Enter the customer's number: "))
    mail = str(input("Does the customer wish to be on the mailing List?(Yes/No) "))

    cus1 = Customer(name, address, phoneNum, cusNum, mail)

    print(f"{devName}, here is the customer, {name}'s information: ")
    print("Name: " + cus1.getName())
    print("Address: " + cus1.getAddress())
    print("Phone number: " + cus1.getPhoneNum())
    print("Customer number: " + cus1.getCusNum())
    print("On Mailing List: " + cus1.getMail())


main()
