from users import add_user, get_users, users

def test_add_user():
    users.clear()
    user = add_user("Ali")
    assert user["name"] == "Ali"
    assert user["id"] == 1

def test_get_users():
    users.clear()
    add_user("Ali")
    add_user("Ayşe")
    result = get_users()
    assert len(result) == 2
