import string
import random 

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
        return self.__amount_withdraw_or_deposit

    def get_new_balance(self):
        return self.__new_balance

    def set_index(self, index):
        slef.__index = index

    def set_type(self, type_):
        self.__type = type_

    def set_amount_withdraw_or_deposit(self, amount):
        self.__amount_withdraw_or_deposit = amount
    
    def set_new_balance(self, balance):
        self.__new_balance = balance


class BankAccout:
    
    def __init__(self, first_name, last_name, initial_deposit, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__curr_amount_of_money = initial_deposit
        self.__history_of_transactions = []
        self.__password_salt = self.__random_salt_generation(len(password))
        self.__password = self.__hash_and_salt_password(password)
        
    def __str__(self):
        return " " + self.__first_name + self.__last_name + " "

    def __hash_and_salt_password(self, password):
        hashed_password = 0
        for i in range(0, len(password)):
            hashed_password += (ord(password[i]) << i) + (ord(self.__password_salt[i]) << i)
        return hashed_password

    def __random_salt_generation(self, size, chars = string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def __save_transaction(self, is_deposit, amount):
        add = amount if is_deposit else -amount    
        self.__history_of_transactions.append(Transaction(len(self.__history_of_transactions) + 1, is_deposit, amount, self.__curr_amount_of_money + add))

    def check_password(self, password):
        curr_hashed_password = self.__hash_and_salt_password(password)
        if curr_hashed_password == self.__password:
            return True
        return False

    def change_password(self, password):
        self.__password_salt = self.__random_salt_generation(len(password))
        self.__password = self.__hash_and_salt_password(password)

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
            curr_transaction_type = "deposit" if curr_transaction.get_type() else "withdraw"
            print("transaction " + str(curr_transaction.get_index()) + " type - " + curr_transaction_type + " amount " + str(curr_transaction.get_amount_withdraw_or_deposit()) +  " new balance " +  str(curr_transaction.get_new_balance()))

    def set_first_name(self, name):
        self.__first_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_curr_amount_of_money(self, amount):
        self.__curr_amount_of_money = amount

    def get_history_of_transactions(self, transactions):
        self.__history_of_transactions = transactions

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_curr_amount_of_money(self):
        return self.__curr_amount_of_money

    def get_history_of_transactions(self):
        return self.__history_of_transactions
