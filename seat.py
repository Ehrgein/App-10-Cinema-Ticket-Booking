import sqlite3

from creator import Creator

class Seat(Creator):

    def __init__(self, seat, name):
        self.seat = seat
        self.name = name

    @classmethod
    def is_free(self):
        connection = Creator.database
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "seat_id" FROM "Seat" WHERE "price"==0
        """)
        result = cursor.fetchall()[0][0]
        connection.close()
        return "The following seats are free!: " + str(result)

    def availability(self):
        connection = self.database
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat])
        self.seatavail = cursor.fetchall()[0][0]
        if self.seatavail == 0:
            return self.buy_ticket()
        else:
            print("Seat is occupied, please try another seat")



    def buy_ticket(self):
        connection = self.database
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM "Banking" WHERE "user"= ?
        """, [self.name])
        self.balance = float(cursor.fetchone()[0])
        cursor.execute("""
        SELECT "price" FROM "Seat" WHERE "seat_id" = ?
        """, [self.seat])
        self.ticketprice = float(cursor.fetchone()[0])

        if self.balance > self.ticketprice:
            print("Ticket purchase succesful!")
        else: 
            print("Not enough balance")
        
        return self.banking_operations()


    def banking_operations(self):

        newbalance = self.balance - self.ticketprice
        connection = self.database
        connection.execute("""
        UPDATE "Banking" SET "balance"=? WHERE "user"=?
        """, [newbalance, self.name])
        connection.commit()
        connection.close()
    
    


        

freeseats = Seat.is_free()

#seat = input("Enter your preffered seat:")
#name = input("Enter your username: ")
#input1 = Seat(seat, name)


#input1.availability()

print(freeseats)

