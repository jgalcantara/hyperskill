class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def __str__(self):
        return f"""\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money"""

    def checker(self, water2, milk2, coffee_beans2, disposable_cups2, money2):
        original_list = [self.water, self.milk, self.coffee_beans, self.disposable_cups]
        coffee_list = [water2, milk2, coffee_beans2, disposable_cups2]
        word_list = ['water', 'milk', 'coffee beans', 'disposable cups']
        counter = 0
        for i in range(len(word_list)):
            if original_list[i] >= coffee_list[i]:
                counter += 1
                continue
            else:
                print(f"Sorry, not enough {word_list[i]}!")
                break
        if counter == len(word_list):
            self.water -= water2
            self.milk -= milk2
            self.coffee_beans -= coffee_beans2
            self.disposable_cups -= disposable_cups2
            self.money += money2
            print("I have enough resources, making you a coffee!")

    def buy(self):
        coffee = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee == "1":  # espresso
            self.checker(250, 0, 16, 1, 4)
        elif coffee == "2":  # latte
            self.checker(350, 75, 20, 1, 7)
        elif coffee == "3":  # cappuccino
            self.checker(200, 100, 12, 1, 6)
        elif coffee == "back":
            self.choice()

    def choice(self):
        action = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            print(self)
        elif action == "exit":
            exit()

    def fill(self):
        fwater = int(input("\nWrite how many ml of water do you want to add:\n"))
        self.water += fwater
        fmilk = int(input("Write how many ml of milk do you want to add:\n"))
        self.milk += fmilk
        fcoffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.coffee_beans += fcoffee_beans
        fdisposable_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.disposable_cups += fdisposable_cups

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


kopi = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    kopi.choice()
