import time

from selenium.webdriver.common.by import By

from pageObject.basePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    SubscribeButton = (By.XPATH, "//button[contains(text(),'Subscribe')]")
    SubscribeInputText = (By.XPATH, "//input[@id='email']")
    subscribeText = (By.XPATH, "//div[contains(text(),'your email already subscribed')]")
    LoginTab = (By.XPATH, "//a[normalize-space()='Log In']")
    HeaderLoginText = (By.XPATH, "//h2[normalize-space()='Log In']")

    UsernameXpath = (By.XPATH, "//div[@class='input-groups undefined'][1]/input")
    PasswordXpath = (By.XPATH, "//input[@type='password']")
    LoginButton = (By.XPATH, "//button[contains(text(),'Log In')]")
    AlertTextLogin = (By.XPATH, "//div[contains(text(),'Login Successfully')]")

    def go_to_subscribePage(self, emaiID):
        self.send_keys(self.SubscribeInputText, emaiID)
        self.click(self.SubscribeButton)
        self.wait_for(self.subscribeText)
        print(self.get_text(self.subscribeText))

    def go_to_login_tab(self):
        self.click(self.LoginTab)
        self.wait_for(self.HeaderLoginText)

    def login_to_application(self, userName, pasWord):
        self.send_keys(self.UsernameXpath, userName)
        self.send_keys(self.PasswordXpath, pasWord)
        self.click(self.LoginButton)
        self.wait_for(self.AlertTextLogin)
        print(self.get_text(self.AlertTextLogin))
