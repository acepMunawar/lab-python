class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    def get_balance(self):
        return self.__balance
    
    def topup(self, amount):
        self.__balance += amount

    def cashout(self, amount):
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount

eko_account = BankAccount("eko")
eko_account.topup(1000000)
print(eko_account.get_balance())
eko_account.cashout(500000)
print(eko_account.get_balance())