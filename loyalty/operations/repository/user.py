from operations.models import User
from operations import serializers


def _get_user(id):
    return User.objects.get(id=id)


def add_balance(id, amount):
    user = User.objects.get(id=id)
    user.balance += amount
    user.save()
    return user.balance


def get_balance(id):
    user = User.objects.get(id=id)
    return user.balance


def sub_balance(id, amount):
    user = User.objects.get(id=id)
    user.balance -= amount
    user.save()
    return user.balance

def get_all_users():
    users = User.objects.all()
    serializer = serializers.UserSerializer(users, many=True)
    return serializer.data

def overall_balance():
    users = get_all_users()
    balance = 0
    for i in users:
        balance += i['balance']
    if balance > 10000:
        return balance
    else: return "no 1000k"


def get_0_users():
    users = get_all_users()
    user_list = []
    for i in users:
        if i['balance'] == 0:
            user_list.append(i)
    return user_list



def get_1000_users():
    users = get_all_users()
    user_list = []
    for i in users:
        if i['balance'] > 1000:
            user_list.append(i)
    return user_list
