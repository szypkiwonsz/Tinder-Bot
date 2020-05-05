class TinderPopups:

    def tinder_notifications(self):
        notification_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        notification_btn.click()

    def tinder_localization(self):
        localization_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        localization_btn.click()

    def keep_going(self):
        keep_going_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        keep_going_btn.click()

    def popup_start_screen(self):
        keep_going_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        keep_going_btn.click()

    def verify_email(self):
        remind_later = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/button[2]')
        remind_later.click()

    def passport(self):
        no_thank_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        no_thank_btn.click()

    def cookies(self):
        agree_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div[1]/button')
        agree_btn.click()
