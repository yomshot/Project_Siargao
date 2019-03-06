import pytest
from PageObject.loginForm import Login

@pytest.mark.usefixtures("setup")
class TestLoginForm:

    def test_login(self):
        driver = self.driver
        run = Login(driver)

        username = "#"
        password = "#"

        run.login(username, password)
