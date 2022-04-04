from operations.celery import app
from operations.models import User


@app.task
def count_balance():
    from operations.repository import user

    balance = 0
    users = user.get_all_users()
    for i in users:
        balance += i['balance']
    return f"count balance {balance}"


@app.task
def count_balance_beat():
    from operations.repository import user

    balance = 0
    users = user.get_all_users()
    for i in users:
        balance += i['balance']
    return f"count balance {balance}"


@app.task
def check_balance(id):
    user = User.objects.get(id=id)
    if user.balance == 0:
        return f'{user.username} have 0 balance'
    elif user.balance == 1000:
        return f'{user.username} have 1000 balance'
