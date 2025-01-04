from .base_locators import BaseLocators

class SignupLoginPageLocators(BaseLocators):
    EMAIL_BTN = BaseLocators.css('button[data-testid="social-auth-button-email"]')
    EMAIL_INPUT = BaseLocators.css('input[id="email-login-email"]')
    CONTINUE_BTN = BaseLocators.css('button[data-testid="signup-login-submit-btn"]')
    PASSWORD_INPUT = BaseLocators.css('input[data-testid="email-signup-password"]')
    LOGIN_BTN = BaseLocators.css('button[data-testid="signup-login-submit-btn"]')
    AGREE_AND_CONTINUE_BTN = BaseLocators.css('button[data-testid="cc-accept"]')
    PROFILE_IMG = BaseLocators.css('button[data-testid="cypress-headernav-profile"] img')
