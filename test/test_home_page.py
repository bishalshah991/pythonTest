import pytest
import softest as softest

from pageObject.home_page import HomePage
from TestData.DamaskTestData import DataTest


@pytest.mark.usefixtures("setup")
class TestHomePage(softest.TestCase):
    def test_homePage(self):
        self.home = HomePage(self.driver)
        self.home.go_to_subscribePage(DataTest.email)
        self.home.go_to_login_tab()
        Email = DataTest.uname
        EmailPassword = DataTest.pwd
        self.home.login_to_application(Email,EmailPassword)
