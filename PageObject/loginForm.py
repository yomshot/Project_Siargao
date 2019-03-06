from Utility.actionKeys import MakeAction
import time

class Login(object):

    findBy = 'xpath'
    loc_username = "//input[@name='email']"
    loc_password = "//input[@name='password']"
    loc_btnLogin = "//span[contains(text(), 'Log In')]"

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)

    def setUsername(self, username):
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.loc_username, 3, username)

    def setPassword(self, password):
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.loc_password, 3, password)

    def clickLogin(self):
        time.sleep(2)
        self.run.click_element(self.findBy, self.loc_btnLogin, 3)

    def login(self, username, password):
        self.setUsername(username)
        self.setPassword(password)
        self.clickLogin()