import random
import sqlite3
conn = sqlite3.connect('card.s3db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS card
             (id INTEGER,
             number TEXT,
             pin TEXT,
             balance INTEGER DEFAULT 0)''')


class Card:

    def __init__(self):
        self.number = 0
        self.pin = 0
        self.balance = 0

    def choice(self):
        choice = int(input("""
1. Create an account
2. Log into account
0. Exit
"""))
        if choice == 1:
            self.one()
        elif choice == 2:
            self.two()
        elif choice == 0:
            print("\nBye!")
            conn.close()
            exit()

    @staticmethod
    def luhn(number_x):
        number_c = number_x[:]
        number_c = [int(number_c[i]) * 2 if i % 2 == 0 else int(number_c[i]) for i in range(len(number_c) - 1)]
        number_c = [number_c[i] - 9 if number_c[i] > 9 else number_c[i] for i in range(len(number_c))]
        number_x[-1] = str(10 - (sum(number_c) % 10)) if (sum(number_c) % 10 != 0) else '0'
        number_x = "".join(number_x)
        return number_x

    def one(self):
        number = list(str("400000" + (str(random.randint(0000000000, 9999999999))).zfill(10)))
        number = self.luhn(number)
        self.number = "".join(number)
        self.pin = ''.join([str(n) for n in random.sample(range(9), 4)])
        c.execute("INSERT INTO card (number, pin) VALUES (?, ?)", (self.number, self.pin))
        conn.commit()
        print("\nYour card has been created")
        print(f"Your card number:\n{self.number}")
        print(f"Your card PIN:\n{self.pin}")

    def two(self):
        test_number = input("\nEnter your card number:\n")
        test_pin = input("Enter your PIN:\n")
        c.execute("SELECT * FROM card WHERE (number = ? AND pin = ?)", (test_number, test_pin))
        result = c.fetchone()
        if (result is None) or (result[1] != test_number) or (result[2] != test_pin):
            print("\nWrong card number or PIN!")
        elif (result[1] == test_number) and (result[2] == test_pin):
            self.number, self.pin = result[1], result[2]
            print("\nYou have successfully logged in!")
            self.two_choice()

    def two_choice(self):
        while True:
            c.execute("SELECT * FROM card WHERE (number = ? AND pin = ?)",
                      (self.number, self.pin))
            row = c.fetchone()
#            self.number, self.pin, self.balance = row[1], row[2], row[3]
            t_choice = int(input("""
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""))
            if t_choice == 1:
                print(f"\nBalance: {row[3]}")
            elif t_choice == 2:
                income = int(input("\nEnter income:\n"))
                c.execute("""UPDATE card SET balance = balance + ?
                WHERE (number = ? AND pin = ?)""", (income, row[1], row[2]))
                conn.commit()
                print("Income was added!")
            elif t_choice == 3:
                print("\nTransfer")
                test_number = input("Enter card number:\n")
                c.execute("SELECT number FROM card WHERE (number = ?)",
                          (test_number,))
                test_fetch = c.fetchone()
                t_number = self.luhn(list(test_number))
                if test_number == row[1]:
                    print("You can't transfer money to the same account!")
                elif test_number != t_number:
                    print("Probably you made mistake in the card number. Please try again!")
                elif test_fetch is None:
                    print("Such a card does not exist.")
                elif (test_number == t_number) and (test_number == test_fetch[0]):
                    money_transfer = int(input("Enter how much money you want to transfer:\n"))
                    if row[3] > money_transfer:
                        c.execute("""UPDATE card SET balance = balance + ?
                        WHERE (number = ?)""", (money_transfer, test_number))
                        c.execute("""UPDATE card SET balance = balance - ?
                        WHERE (number = ?)""", (money_transfer, row[1]))
                        print("Success!")
                        conn.commit()
                    else:
                        print("Not enough money!")
            elif t_choice == 4:
                c.execute("DELETE FROM card WHERE (number = ? AND pin = ?)", (row[1], row[2]))
                conn.commit()
                print("\nThe account has been closed!")
                break
            elif t_choice == 5:
                print("\nYou have successfully logged out!")
                break
            elif t_choice == 0:
                print("\nBye!")
                conn.close()
                exit()


while True:
    Card().choice()
