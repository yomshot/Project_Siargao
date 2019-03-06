from selenium.webdriver import Chrome
import pytest
import time

@pytest.fixture(scope="class")
def setup(request):

    url = 'https://chain.unionbankph.com'
    path = 'D:\\chromedriver.exe'

    driver = Chrome(executable_path=path)
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    # time.sleep(10)
    driver.close()