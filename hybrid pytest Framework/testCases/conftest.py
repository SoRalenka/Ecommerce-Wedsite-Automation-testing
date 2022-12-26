from selenium import webdriver 
import pytest
from selenium.webdriver.common.service import Service

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\Users\\sourabh\\OneDrive\\Documents\\browser specific driver\\chromedriver.exe" )
        print('launching chrome browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox("C:\\Users\\sourabh\\OneDrive\\Documents\\browser specific driver\\geckodriver.exe")
        print('launching chrome firefox')
    else :
        driver = webdriver.Chrome("C:\\Users\\sourabh\\OneDrive\\Documents\\browser specific driver\\chromedriver.exe" )
        print('launching chrome browser')       
    return driver


def pytest_addoption(parser): #this will get the value from CLI /hooks
    parser.addoption("--browser")
        
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


###############pytest html report ###################3

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sourabh'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)