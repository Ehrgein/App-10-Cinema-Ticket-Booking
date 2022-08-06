import sqlite3



class Creator:

    database = sqlite3.connect("cinema.db")
 
   
    @classmethod
    def create_user_table(self):
        """
        Create a table with user's credit card information
        """
        connection = self.database
        connection.execute("""
        CREATE TABLE "Card Information"(
            "type" TEXT,
            "number" TEXT,
            "cvc" TEXT,
            "holder" TEXT,
            "balance" REAL
        );
        """)

    @classmethod
    def create_seat(self):
        """
        Create a table with information about the cinema's seats
        """
        connection = self.database
        connection.execute("""
        CREATE TABLE "Seat" (
            "seat_id" TEXT,
            "taken" INTEGER,
            "price" REAL
        );
        """)

    def create_banking_table(self):

        connection = self.database
        connection.execute("""
        CREATE TABLE "Banking"(
            "user" TEXT,
            "balance" REAL
        );
        """)


    def insert_seats(self, seat_id, occupied, price):
        """
        Insert information abotu the seats in a table
        """
        connection = sqlite3.connect(self.database)
        connection.execute("""
        INSERT INTO "Seat" (seat_id, taken, price)
        VALUES (?, ?, ?)""", (seat_id, occupied, price))
        connection.commit()
        connection.close()


"""
 Creator.create_user_table()
"""
# Instanciating the Creator class to call the create_user_table function

