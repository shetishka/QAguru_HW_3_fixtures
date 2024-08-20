import pytest

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"

def test_logout(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"
