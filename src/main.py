from User import User
from Device import Device
from Database import Database
from Login import Login
from Controller import Controller

def main():

    myController    = Controller()
    myLoginView     = Login(myController)

if __name__ == '__main__':
    main()
