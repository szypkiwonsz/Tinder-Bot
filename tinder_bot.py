from selenium import webdriver
from time import sleep
from login_buttons import TinderLogin, FacebookLogin
from popups import TinderPopups
from functions import TinderFunctions


class TinderBot(TinderLogin, FacebookLogin, TinderPopups, TinderFunctions):
    def __init__(self):
        self.driver = webdriver.Chrome()

    # Login to tinder which includes Facebook login attempt.
    def login(self):
        self.driver.get("https://tinder.com/app")
        sleep(6)

        # First try with hidden Facebook login button.
        self.more_option_btn_click()
        sleep(2)
        try:
            self.more_option_fb_btn_click()
            try:
                # Checking if the user is already logged in to the site.
                self.tinder()
            except Exception:
                # If not, Facebook login attempt.
                self.login_facebook()
                self.tinder()

        # If the selected button has not been found, try logging in again with a different button setting.
        except Exception:
            self.account_recovery_exit_btn()
            self.login_btn()
            try:
                self.fb_btn()
                try:
                    self.tinder()
                except Exception:
                    self.login_facebook()
                    self.tinder()
            except Exception:
                # If the Facebook login button was not found, it displays a message.
                print("Try again after 30 seconds.")

    def login_facebook(self):
        # Changing the window to the login window via Facebook
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.fb_email_in()
        self.fb_password_in()
        self.fb_login_btn()
        # Changing the window to the main window
        self.driver.switch_to.window(base_window)

    def tinder(self):
        sleep(5)
        try:
            self.tinder_localization()
        except Exception:
            pass

        self.tinder_notifications()

    def like(self):
        while True:
            try:
                sleep(0.4)
                self.swipe_right()
            except Exception:
                try:
                    sleep(0.4)
                    self.send_message('<3')
                    ''' Option without sending message '''
                    # self.keep_going()
                except Exception:
                    sleep(0.4)
                    self.popup_start_screen()


if __name__ == "__main__":
    bot = TinderBot()
    bot.login()
    sleep(2)
    try:
        bot.like()
    except Exception:
        try:
            bot.verify_email()
            bot.like()
        except Exception:
            try:
                bot.passport()
                bot.like()
            except Exception:
                bot.cookies()
                bot.passport()
                bot.like()
