from selene import browser, be, have
import pytest



def test_search_positive(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_negative(browser_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('chmegamogl').press_enter()
    browser.element('[id="botstuff"]').should(have.text('По запросу chmegamogl ничего не найдено. '))