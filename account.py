import hashlib
import random
from db import customer_db
class Account:

    def __init__(self, fname=None, lname=None, email=None, passcode=None, pin=None, bvn=None):
        self.__fname = fname
        self.__lname = lname
        self.__phone_no = None
        self.__email = email
        self.__pin = pin
        self.__passcode = passcode
        self.__address:str = None

        if bvn == None:
            self.__bvn = str(random.randint(10000000000, 99999999999))
        else:
            self.__bvn = bvn

        self.__balance = 0.0
        self.__account_no = "888" + str(random.randint(1000000, 9999999))
        self.__nin:str = None

    def get_fname(self):
        return self.__fname

    def set_fname(self, fname:str):
        assert type(fname) == str, "Only strings allowed for First name"
        self.__fname = fname

    def get_lname(self):
        return self.__lname

    def set_lname(self, lname:str):
        assert type(lname) == str, "Only strings allowed for Last name"
        self.__lname = lname

    def get_phone_no(self):
        return self.__phone_no

    def set_phone_no(self, phone:str):
        assert type(phone) == str, "Only strings allowed for Phone number"
        self.__phone_no = phone

    def get_email(self):
        return self.__email

    def set_email(self, email:str ):
        assert type(email) == str, "Only strings allowed for Email"
        self.__email = email

    def set_pin(self, new_pin: str):
        assert type(new_pin) == str, "New Pin provided is not a string value"
        assert new_pin.isnumeric(), "Pin provided should contain only numbers"

        self.__pin = new_pin

    def set_passcode(self, new_passcode: str):
        assert type(new_passcode) == str, "New passcode provided is not a string value"

        self.__passcode = hashlib.md5(new_passcode.encode('utf-8')).hexdigest()

    def get_address(self):
        return self.__address

    def set_address(self, address):
        assert type(address) == str, "New address provided is not a string value"

        self.__address = address

    def get_bvn(self):
        return self.__bvn

    def get_balance(self):
        return self.__balance

    def get_account_no(self):
        return self.__account_no

    def get_nin(self):
        return self.__nin

    def set_nin(self, nin):
        assert type(nin) == str, "NIN provided is not a string value"
        assert nin.isnumeric(), "NIN provided should contain only numbers"

        self.__nin = nin


    def withdraw(self, amount: float) -> float:
        assert type(amount) == float, "Amount to withdraw must be a number"
        assert amount > 0, "Amount to must be a positive number"
        assert amount <= self.__balance, "Insufficient funds"

        self.__balance -= amount

        print(f"""
        Debit:
        Withdrawn N{amount} successfully!
        New Balance: N{self.__balance}
""")
        return self.__balance


    def deposit(self, amount:float)-> float:
        assert type(amount) == float, "Amount to be deposited must be a number"
        assert amount > 0, "Amount to deposti must be positive"

        self.__balance += amount

        print(f"""
        Credit:
        Deposited N{amount} successfully!
        New Balance: N{self.__balance}
""")
        return self.__balance

    def transfer(self, amount:float, acc_no:str):
        beneficiary:Account = customer_db.get(acc_no, None)
        assert beneficiary is not None, "404 User does not exist"

        self.withdraw(amount)
        beneficiary.deposit(amount)
        return self.__balance











