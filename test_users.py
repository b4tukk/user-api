from users import add_user, get_users, delete_user, users

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

def test_delete_user_success():
    users.clear()
    user = add_user("Veli")
    result = delete_user(user["id"])
    assert result is True
    assert len(users) == 0

def test_delete_user_not_found():
    users.clear()
    add_user("Zeynep")
    result = delete_user(999)
    assert result is False
    assert len(users) == 1
