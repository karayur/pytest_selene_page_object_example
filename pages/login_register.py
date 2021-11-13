from typing import Protocol

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.page_elements import CheckBox, PasswordTextBox, TextBox, Button
from tests.value_objects import UsernameAndPassword

# General locators
LOCATOR_USERNAME = (By.ID, "username")
LOCATOR_SHOW_PASSWORD_CHECKBOX = (By.ID, "show-password")

# Login specific locators
LOCATOR_PASSWORD_LOGIN = (By.ID, "password")
LOCATOR_LOG_IN_BTN = (By.CSS_SELECTOR, 'input[value="Log in"]')

# Register specific locators
LOCATOR_NAME = (By.ID, "name")
LOCATOR_EMAIL = (By.ID, "email")
LOCATOR_PASSWORD_REGISTER = (By.ID, "new_password")
LOCATOR_PASSWORD_CONFIRM = (By.ID, "password_confirm")
LOCATOR_CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, 'input[data-target="password-match.submit"]')


# https://andrewbrookins.com/technology/building-implicit-interfaces-in-python-with-protocol-classes/
# https://mypy.readthedocs.io/en/latest/more_types.html#mixin-classes
# https://stackoverflow.com/questions/51930339/how-do-i-correctly-add-type-hints-to-mixin-classes

#
# class HasUsernamePasswordShow(Protocol):
#     @property
#     def username(self) -> TextBox: ...
#
#     @property
#     def password(self) -> PasswordTextBox: ...
#
#     @property
#     def show_password_checkbox(self) -> CheckBox: ...


# class UsernamePasswordShowMixin:
#
#     def enter_username(self: HasUsernamePasswordShow, username):
#         self.username.enter_text(username)
#
#     def enter_password(self: HasUsernamePasswordShow, password):
#         self.password.enter_text(password)
#
#     def toggle_show_password(self: HasUsernamePasswordShow):
#         self.show_password_checkbox.toggle()
#
#     def is_password_masked(self: HasUsernamePasswordShow):
#         return self.password.is_type_password()


class UsernamePasswordShowMixin:

    def enter_username(self, username):
        self.username.enter_text(username)

    def enter_password(self, password):
        self.password.enter_text(password)

    def toggle_show_password(self):
        self.show_password_checkbox.toggle()

    def is_password_masked(self):
        return self.password.is_type_password()


class Login(BasePage, UsernamePasswordShowMixin):

    def __init__(self, driver):
        super().__init__(driver)
        # self.username = TextBox(self.find_element(LOCATOR_USERNAME))
        self.password = PasswordTextBox(self.find_element(LOCATOR_PASSWORD_LOGIN))
        self.show_password_checkbox = CheckBox(self.find_element(LOCATOR_SHOW_PASSWORD_CHECKBOX))
        self.log_in_button = Button(self.find_element(LOCATOR_LOG_IN_BTN))

    def log_in(self, username_and_password: UsernameAndPassword):
        self.enter_username(username_and_password.username)
        self.enter_password(username_and_password.password)
        self.log_in_button.click()


class Register(BasePage, UsernamePasswordShowMixin):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = TextBox(self.find_element(LOCATOR_PASSWORD_CONFIRM))
        self.email = TextBox(self.find_element(LOCATOR_PASSWORD_REGISTER))
        self.password = PasswordTextBox(self.find_element(LOCATOR_PASSWORD_REGISTER))
        self.confirm_password = PasswordTextBox(self.find_element(LOCATOR_PASSWORD_CONFIRM))
        self.show_password_checkbox = CheckBox(self.find_element(LOCATOR_SHOW_PASSWORD_CHECKBOX))
        self.create_account = self.find_element(LOCATOR_CREATE_ACCOUNT_BTN)

    def enter_name(self, name):
        self.name.enter_text(name)

    def enter_email(self, email):
        self.email.enter_text(email)

    def enter_password_confirm(self, password):
        self.confirm_password.enter_text(password)

    def is_confirm_password_masked(self):
        return self.confirm_password.is_type_password()
