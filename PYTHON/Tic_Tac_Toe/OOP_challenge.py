class Account:
    def __init__(self, owner, balance) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return ("Account owner : " + self.owner + "\n" +
                "Account balance : " + str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit : " + str(self.balance))

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Withdrawal denied, not enough balance")
        else:
            self.balance -= amount
            print("Balance after withdrawal : " + str(self.balance))


if __name__ == "__main__":
    my_acc = Account("Vojtěch Ličko", 5000)
    print(my_acc)
    my_acc.withdraw(3000)
    my_acc.deposit(6000)
