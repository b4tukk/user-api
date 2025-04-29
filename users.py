users = []

def add_user(name):
    user = {'id': len(users) + 1, 'name': name}
    users.append(user)
    return user

def get_users():
    return users
