class atm:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, ammount):
        self.balance += ammount
        return self.balance

    def withdraw(self, ammount):
        self.balance -= ammount
        return self.balance


name = input("enter your name: ")
balance = int(input("enter ur balance: "))
account1 = atm(name, balance)

while True:
    print("\n--- ATM Menu ---")
    choice = int(
        input("enter 1 for deposit, 2 for withdraw, 3 check balance, 4 to exit")
    )

    if choice == 1:
        ammount = int(input("enter the ammount: "))
        deposit = account1.deposit(ammount)
        print("deposit successfull, your avail balance:", deposit)

    elif choice == 2:
        ammount = int(input("enter the ammount to withdraw: "))
        if account1.balance >= ammount:
            withdraw = account1.withdraw(ammount)
            print("money withdrawal successfull, avail balance:", withdraw)
        else:
            print("not enough balance")

    elif choice == 3:
        print("Your current balance is:", account1.balance)

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")