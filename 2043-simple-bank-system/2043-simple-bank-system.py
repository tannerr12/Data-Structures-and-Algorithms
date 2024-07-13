class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if not self.validAccount(account1, money) or not self.validAccountNumber(account2):
            return False
        else:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        account -= 1
        if self.validAccountNumber(account):
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        account -=1
        if self.validAccount(account,money):
            self.balance[account] -= money
            return True
        return False
    
    def validAccount(self,acc, bal):
        if acc < len(self.balance) and self.balance[acc] >= bal:
            return True
        return False
    
    def validAccountNumber(self,acc):
        return acc < len(self.balance)

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)