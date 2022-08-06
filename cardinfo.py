import sqlite3
from creator import Creator


class CardInfo(Creator):

    database = Creator.database

    """User registration, creating variables"""
    def __init__(self,type, number, cvc, holder, balance):
        
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        self.balance = balance


    
    def new_user_card(self):

        connection = self.database
        connection.execute("""
        INSERT INTO "Card Information" (type, number, cvc,
        holder, balance)
        VALUES (?, ?, ?, ?, ?)""", (self.type, self.number, 
        self.cvc, self.holder, self.balance))
        connection.commit()
        return self.banking_user()
        

    def banking_user(self):
        connection = self.database
        connection.execute("""
        INSERT INTO "Banking" (user, balance)
        VALUES (?, ?)""", (self.holder, self.balance))
        connection.commit()
        connection.close()
        

#CardInfo.create_banking_table()

""" type = input("Please enter your card type: ")
number = input("Please enter your card number: ")
cvc = input("Please enter your card cvc: ")
holder = input("Please enter the card holder's name: ")
balance = input("Please enter a balance amount to load onto our app: ")

# IT FREAKING WORKS.


newuser = CardInfo(type, number, cvc, holder, balance)

newuser.new_user_card() """


CardInfo.validate()