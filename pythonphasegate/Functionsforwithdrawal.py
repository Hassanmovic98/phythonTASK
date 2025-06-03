acount_balance = int(input('Enter your account balance: '))
list_of_transactions = []
list_of_withdrawals = []
list_of_balance = []

def setup():

    def get_bankapp():
        return "Welcome to Hassan's Bank"

    def get_account_balance(deposit):
        if deposit < 0:
            return "This is invalid"

        if deposit < 100:
            return "deposit is less than 100"

        account_balance = deposit
        list_of_transactions.append(("Deposit amount", deposit))
        list_of_balance.append(account_balance)
        return "Deposit succesful"

    def Withdraw(amount):
       
        if amount < 0:
            return "invalid amount"
        if amount >= 20000:
            return "20k is your daily limit"
        if amount % 500 != 0:
            return "you can only withdraw in 500 mutiples"
        if amount > 0.9 * account_balance:
            return "cant withdraw more than 90%"
        if account_balance - amount < 100:
            return "account balance can't go below 100"

        account_balance -= amount
        list_of_withdrawals.append(amount)
        list_of_transactions.append(("Withdrawn", amount))
        list_of_balance.append(account_balance)
        print("Transaction succesful")
        print("withdrawal:", amount)
        return f"Balance after withdrawal: {account_balance}"

    return {
        "get_bankapp": get_bankapp,
        "get_account_balance": get_account_balance,
        "Withdraw": Withdraw
    }