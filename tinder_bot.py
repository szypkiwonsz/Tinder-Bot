from selenium import webdriver
from time import sleep
from secrets import email, password


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com/app")

        sleep(6)

        more_options_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        more_options_btn.click()

        sleep(2)

        try:
            fb_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button/span[2]')
            fb_btn.click()

            sleep(2)

            try:
                self.tinder()
            except Exception:
                self.login_facebook()
                self.tinder()

        except Exception:
            exit_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
            exit_btn.click()

            sleep(2)

            login_btn = self.driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
            login_btn.click()

            sleep(2)

            try:
                fb_btn = self.driver.find_element_by_xpath(
                    '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
                fb_btn.click()

                sleep(2)

                try:
                    self.tinder()
                except Exception:
                    self.login_facebook()
                    self.tinder()

            except Exception:
                print("Try again after 30 seconds.")

    def login_facebook(self):

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_btn.click()

        sleep(2)

        self.driver.switch_to_window(base_window)

    def tinder(self):

        sleep(6)
        try:
            localization_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/'
                                                                 'button[1]')
            localization_btn.click()
        except Exception:
            print("Wrong email or password!")

        sleep(2)

        notification_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/'
                                                             'button[2]')
        notification_btn.click()

        sleep(2)

    def like(self):

        while True:

            try:
                like_btn = self.driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                like_btn.click()
            except Exception:
                try:
                    self.keep_going()
                except Exception:
                    self.popup_start_screen()

    def keep_going(self):
        keep_going_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        keep_going_btn.click()

    def popup_start_screen(self):
        keep_going_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        keep_going_btn.click()


if __name__ == "__main__":
    bot = TinderBot()
    bot.login()
    bot.like()

