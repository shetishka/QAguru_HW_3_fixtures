import pytest

@pytest.fixture(scope="session")
def browser():
    print('Browser!')
    yield
    print("Close browser!")

@pytest.fixture
def login_page(browser):
    print('Loging passed!')
    pass

@pytest.fixture
def user():
    print('User!')
    return "username", "password"