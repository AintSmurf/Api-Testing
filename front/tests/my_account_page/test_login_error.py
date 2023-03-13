
import pytest
from front.pages.MyAccountSignedOut import MyAccountSignedOut

@pytest.mark.usefixtures("init_driver")
class TestLoginError:

    @pytest.mark.selenium
    @pytest.mark.tcids1
    def test_login_none_existin_user(self):

        #get the url
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()

        # type username
        un = "billy"
        my_account.input_login_username(un)

        #type password
        my_account.input_login_password("123456")

        #click the login button
        my_account.click_login_button()

        #verify error message
        expected_error = f"Error: The username {un} is not registered on this site. If you are unsure of your username, try your email address instead."
        my_account.wait_until_error_is_displayed(expected_error)

