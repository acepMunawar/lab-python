class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    @property
    def balance(self):
        return self.__balance
    
    @property
    def no(self):
        return self.__no

    def topup(self, amount):
        self.__balance += amount

    def cashout(self, amount):
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount

account1 = BankAccount("eko")
print(account1.no)
print(account1.balance)

account1.topup(10000)
print(account1.balance)

account1.cashout(5000)
print(account1.balance)