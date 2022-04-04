from .repository import transaction, user


def add_balance(id, data):
    data['userID'] = id
    saved_transaction = transaction.save(data)
    user.add_balance(id=id, amount=data['amount'])
    return saved_transaction

def get_balance(id):
    user_balance = user.get_balance(id)
    return user_balance

def sub_balance(id, data):
    data['userID'] = id
    saved_transaction = transaction.save(data)
    user.sub_balance(id=id, amount=data['amount'])
    return saved_transaction


def get_overall_balance(data):
    balance = user.overall_balance()
    return balance


def get_0_users():
    users = user.get_0_users()
    return users


def get_1000_users():
    users = user.get_1000_users()
    return users
