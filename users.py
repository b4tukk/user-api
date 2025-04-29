users = []

def add_user(name):
    user = {'id': len(users) + 1, 'name': name}
    users.append(user)
    return user

def get_users():
    return users

def delete_user(user_id):
    global users
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return True
    return False
