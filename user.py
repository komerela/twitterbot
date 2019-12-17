#!/usr/bin/python3
""" 
User class
"""

class User:
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self.__email = 0
    
    @property
    def email(self):
        """ Getter function """
        print("getter method called")
        return self.__email

    @email.setter
    def email(self, email):
        """ Setter Function """
        if type(email) is not str:
            raise TypeError("email must be a string")
        print("setter method called")
        self.__email = email   
    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)