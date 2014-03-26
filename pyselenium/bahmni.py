from selenium.webdriver.common.keys import Keys
from selenium import webdriver



webDriver = webdriver.Firefox()
from test_config import BAHMNI_LOGIN_HOME, BAHMNI_HOME_USERNAME_FIELD_ID, BAHMNI_HOME_PASSWORD_FIELD_ID, \
    BAHMNI_USERINFO_BUTTON, BAHMNI_HOME_SITE_TITLE, BAHMNI_LOGOUT


def login_bahmni_home(web_driver, username, password):
    generic_login(web_driver, BAHMNI_HOME_USERNAME_FIELD_ID, BAHMNI_HOME_PASSWORD_FIELD_ID, username, password, BAHMNI_LOGIN_HOME)
    assert check_title(web_driver, BAHMNI_HOME_SITE_TITLE)

def generic_login(web_driver, username_field_id, password_field_id, username, password, login_url):
    web_driver.get("%s" % login_url)
    web_driver.implicitly_wait(5)
    username_element = web_driver.find_element_by_id(username_field_id)
    password_element = web_driver.find_element_by_id(password_field_id)
    username_element.send_keys(username)
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)

def check_title(web_driver, site_title):
    return site_title in web_driver.title

def check_url(web_driver, url):
    return url in web_driver.current_url

def logout_from_bahmni(web_driver):
    web_driver.implicitly_wait(5)
    userinfo_drop_down = web_driver.find_element_by_class_name(BAHMNI_USERINFO_BUTTON)
    userinfo_drop_down.click()
    logout_link = web_driver.find_element_by_link_text(BAHMNI_LOGOUT)
    logout_link.click()
    assert check_url(web_driver, BAHMNI_LOGIN_HOME)

def do_something():
    pass

