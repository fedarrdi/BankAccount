class Transaction:
    
    def __init__(self, index, type_, amount_withdraw_or_deposit, new_balance):
        self.__index = index
        self.__type = type_
        self.__amount_withdraw_or_deposit = amount_withdraw_or_deposit
        self.__new_balance = new_balance
    
    def get_index(self):
        return self.__index
    
    def get_type(self):
        return self.__type

    def get_amount_withdraw_or_deposit(self):
        return self.__new_balance
        return self.__amount_withdraw_or_deposit

    def get_new_balance(self):

    def set_index(self, index):
        slef.__index = index

    def set_type(self, type_):
        self.__type = type_

    def set_amount_withdraw_or_deposit(self, amount):
        self.__amount_withdraw_or_deposit = amount
    
    def set_new_balance(self, balance):
        self.__new_balance = balance


class BankAccout:
    
    def __init__(self, first_name, last_name, initial_deposit):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__curr_amount_of_money = initial_deposit
        self.__history_of_transactions = []
    
    def __str__(self):
        return " " + self.__first_name + self.__last_name + " "

    def __save_transaction(self, is_deposit, amount):
        add = amount if is_deposit else -amount    
        self.__history_of_transactions.append(Transaction(len(self.__history_of_transactions) + 1, is_deposit, amount, self.__curr_amount_of_money + add))

    def withdraw(self, amount):
        if amount <= self.__curr_amount_of_money:
            self.__save_transaction(False, amount)
            self.__curr_amount_of_money -= amount
            return self.__curr_amount_of_money - amount
        return 0
        
    def deposit(self, amount):
        self.__save_transaction(True, amount)
        self.__curr_amount_of_money += amount

    def print_all_transactions(self):
        for curr_transaction in self.__history_of_transactions:
            curr_transaction_type = "withdraw"
            if curr_transaction.get_type():
                curr_transaction_type = "deposit"
            print("transaction " + str(curr_transaction.get_index()) + " type - " + curr_transaction_type + " amount " + str(curr_transaction.get_amount_withdraw_or_deposit()) +  " new balance " +  str(curr_transaction.get_new_balance()))

    def set_first_name(self, name):
        self.__first_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_curr_amount_of_money(self, amount):
        self.__curr_amount_of_money = amount

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_curr_amount_of_money(self):
        return self.__curr_amount_of_money

my_bank_account = BankAccout("Radoslav", "Filipov", 200)
my_bank_account.deposit(300)
my_bank_account.deposit(1000)
my_bank_account.withdraw(300)
my_bank_account.deposit(1000)
my_bank_account.withdraw(10000)
my_bank_account.print_all_transactions()