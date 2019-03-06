from selenium.webdriver.common.by import By

def method_by(by: str):
    if by == 'xpath':
        return By.XPATH
    elif by == 'class':
        return By.CLASS_NAME
    elif by == 'id':
        return By.ID
    elif by == 'link':
        return By.LINK_TEXT
    elif by == 'css':
        return By.CSS_SELECTOR
    elif by == 'name':
        return By.NAME
    elif by == 'tag_name':
        return By.TAG_NAME
    else:
        raise Exception('Invalid locator method.')
