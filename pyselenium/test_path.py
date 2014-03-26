from test_config import *
from bahmni import *


#Test Config
web_driver =  webdriver.Firefox()

#User Path
login_bahmni_home(web_driver, BAHMNI_HOME_ADMIN_USERNAME, BAHMNI_HOME_ADMIN_PASSWORD)
do_something()
logout_from_bahmni(web_driver)


#Close Test
web_driver.close()