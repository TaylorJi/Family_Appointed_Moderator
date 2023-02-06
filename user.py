from enum import Enum

from bank import Bank
from budget import Budget
from transaction import Transaction


class UserTypes(Enum):
    ANGEL = "Angel"
    TROUBLE_MAKER = "Trouble Maker"
    REBEL = "Rebel"


class User:
    """
    This class manages users' information.
    """
    user_type_list = UserTypes

    # budget in argument is a list of list
    # budget = [[120, 80], [200, 160], [150, 90], [70, 60]] total_budget, budget_limit
    def __init__(self, user_name, user_age, user_type, account_number, budget, balance):
        self._user_name = user_name
        self._user_age = user_age
        self._user_type = user_type
        self._transaction = []
        self._budget = {"GE": Budget("Game and Entertainment", budget[0][0], budget[0][1]),
                        "CA": Budget("Clothing and Accessories", budget[1][0], budget[1][1]),
                        "EO": Budget("Eating Out", budget[2][0], budget[2][1]),
                        "MIS": Budget("Miscellaneous", budget[3][0], budget[3][1])
                        }

        self._bank = Bank(account_number, balance)

    def get_user_name(self):
        return self._user_name

    def get_user_age(self):
        return self._user_age

    def get_user_type(self):
        return self._user_type

    def get_user_bank_account_number(self):
        return self._bank.get_account_number()

    def get_user_bank_balance(self):
        return self._bank.get_balance()

    def get_user_budget(self):
        return self._budget.get_total_budget()

    def get_warning_budget_limit(self):
        return self._budget.get_warning_budget_limit()

    def add_new_user(self):
        pass

    def remove_user(self):
        pass

    def set_user_name(self, name):
        self._user_name = name

    def set_user_age(self, age):
        self._user_age = age

    def set_user_type(self, user_type):
        self._user_type = user_type

    def set_user_bank_account_number(self, account_number):
        self._bank.set_account_number(account_number)

    def set_user_bank_balance(self, balance):
        self._bank.set_balance(balance)

    def set_user_budget(self, budget):
        self._budget.set_total_budget(budget)

    def set_warning_budget_limit(self, budget_limit):
        self._budget.set_warning_budget_limit(budget_limit)
