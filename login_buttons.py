from secrets import email, password


class TinderLogin:

    def more_option_btn_click(self):
        more_options_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        more_options_btn.click()

    def more_option_fb_btn_click(self):
        fb_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button/span[2]')
        fb_btn.click()

    def account_recovery_exit_btn(self):
        exit_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        exit_btn.click()

    def login_btn(self):
        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_btn.click()

    def fb_btn(self):
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()


class FacebookLogin:

    def fb_email_in(self):
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

    def fb_password_in(self):
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys(password)

    def fb_login_btn(self):
        fb_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_btn.click()
