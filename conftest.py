import pytest
from selene import browser, be, have

@pytest.fixture(scope="session")
def browser_size():
    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920  # задает ширину окна браузера
    yield
    browser.quit()

@pytest.fixture(scope="session")
def browser_example():
    browser.open('https://google.com')
    yield


@pytest.fixture
def login_page(browser_example):
    print('Loging passed!')
    pass

@pytest.fixture
def user():
    print('User!')
    return "username", "password"