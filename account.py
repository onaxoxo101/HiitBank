import _md5
import random


class Account:

    def __init__(self,fname,lname,email,pin,passcode,bvn,account):
        self.__fname = fname
        self.__lname = lname
        self.__phone_no = None
        self.__email = email
        self.__pin = pin
        self.__passcode = passcode
        self.__account_no = "888" + str(random.randint(1000000, 9999999))
        self.__bvn = bvn
        self.__balance = 0.0
        self.__nin = None
        self.__address = None

        if bvn == None:
            self.__bvn = str(random.randint(100000000, 9999999999))
        else:
            self.__bvn = bvn

    def get_fname(self):
        return self.__fname

    def set_fname(self,fname):
        assert type(fname) == str, 'only strings allowed for first name'
        self.__fname = fname

    def get_lname(self):
        return self.__lname

    def set_lname(self, lname):
        assert type(lname) == str, 'only strings allowed last name'
        self.__lname = lname

    def get_phone_no(self):
        return self.__phone_no

    def get_email(self):
        return self.__email

    def set_email(self,email):
        assert type(email) == str, 'only strings allowed for email'
        self.__email = email


    def set_pin(self, new_pin):
        assert type(new_pin) == str, 'New pin provided is not a string value'
        assert str(new_pin).isnumeric(), 'pin provided should contain 8 letters with first uppercase and one numerical number'

        self.__pin = new_pin


    def set_passcode(self,new_passcode):
        assert type(new_passcode) == str, 'new passcode provided is not a string value '

        self.__passcode = _md5.md5(new_passcode)

    def get_bvn(self):
        return self.__bvn


    def set_address(self,address):
        assert type(address) == str, 'address should be in string'
        self.__address = address

    def get_balance(self):
        return self.__balance

    def get_account_no(self):
        return self.__account_no

    def set_nin(self, nin:str):
        assert type(nin) == str, 'nin must be a string'
        assert nin.isnumeric(), 'nin must be numeric'
        self.__nin = None



    def withdraw(self, amount:float) -> float:
        assert type(amount) == float, 'amount to withdraw must be numeric'
        assert amount > 0, 'amount to withdraw must be a positive number'
        assert amount < self.__balance, 'insufficient funds'

        self.__balance -= amount
        return self.__balance








