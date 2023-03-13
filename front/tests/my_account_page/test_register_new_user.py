import pytest
from front.pages.MyAccountSignedOut import MyAccountSignedOut
from front.pages.MyAccountSignedIn import MyAccountSignedIn
from front.helpers.MyAcccountHelper import gernerate_random_email,generate_random_username

@pytest.mark.usefixtures("init_driver")
class TestLoginError:

    @pytest.mark.selenium
    @pytest.mark.tcids2
    def test_register_new_user(self):

        #get the url
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()

        # fill in username
        my_account.input_register_username(generate_random_username())

        #fill in email
        my_account.input_register_email(gernerate_random_email())

        #click the register button
        my_account.click_register_button()

        #verify error message
        my_account_in = MyAccountSignedIn(self.driver)
        my_account_in.wait_until_logout_locator_clickable()

    @pytest.mark.selenium
    @pytest.mark.tcids3
    def test_register_new_user_failed(self):

        #get the url
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()

        # fill in username
        my_account.input_register_username('Maryjane Blackwell')

        #fill in email
        my_account.input_register_email('wvtjuoerbjswrwl@test.com')

        #click the register button
        my_account.click_register_button()

        #verify error message
        expected_error =" Error: An account is already registered with your email address. Please log in."
        my_account.wait_until_register_error_pops_up(expected_error)
