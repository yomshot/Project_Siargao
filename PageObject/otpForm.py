from Utility.actionKeys import MakeAction
import time

class Otp(object):

    findBy = "xpath"

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)

    def run_otp(self):
        time.sleep(2)
        for i in range(6):
            fld_otp = "//input[@name='digit{0}']".format(i)
            self.run.find_element_and_input(self.findBy, fld_otp, 3, "1")
