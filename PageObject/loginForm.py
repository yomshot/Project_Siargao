from Utility.actionKeys import MakeAction
from .otpForm import Otp
import time

class Login(object):

    findBy = 'xpath'
    fld_username = "//input[@name='email']"
    fld_password = "//input[@name='password']"
    fld_btnLogin = "//span[contains(text(), 'Log In')]"

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)
        self.otp = Otp(driver)

    def setUsername(self, username):
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.fld_username, 3, username)

    def setPassword(self, password):
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.fld_password, 3, password)

    def clickLogin(self):
        time.sleep(2)
        self.run.click_element(self.findBy, self.fld_btnLogin, 3)

    def login(self, username, password):
        self.setUsername(username)
        self.setPassword(password)
        self.clickLogin()
        self.otp.run_otp()
        time.sleep(5)