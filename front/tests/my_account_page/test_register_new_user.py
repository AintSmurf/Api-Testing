import pytest
from front.pages.MyAccountSignedOut import MyAccountSignedOut
from front.pages.MyAccountSignedIn import MyAccountSignedIn
from backend.src.dao.customers_dao import CustomersDAO
from backend.src.utilities.genericUtilities import generate_random_email_and_password, generate_random_username

@pytest.mark.usefixtures("init_driver")
class TestLoginError:

    @pytest.mark.selenium
    @pytest.mark.tcids2
    def test_register_new_user(self):
        #get the url
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()

        #generate random cusomer
        cs = generate_random_email_and_password()

        #fill in email
        my_account.input_register_email(cs['email'])

        #fill in password
        my_account.input_register_password(cs['password'])

        #click the register button
        my_account.click_register_button()

        #verify error message
        my_account_in = MyAccountSignedIn(self.driver)
        my_account_in.wait_until_logout_locator_clickable()

    @pytest.mark.selenium
    @pytest.mark.tcids3
    def test_register_new_user_failed(self):
        #db object
        cs_dao = CustomersDAO()
        email = cs_dao.get_random_customer_by_email()[0]['user_email']

        #get the url
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()

        #fill in email
        my_account.input_register_email(email)

        #fill in password
        my_account.input_register_password("123456dasdaAdasdasdas")

        #click the register button
        my_account.click_register_button()


        #verify error message
        expected_error =" Error: An account is already registered with your email address. Please log in."
        my_account.wait_until_register_error_pops_up(expected_error)
