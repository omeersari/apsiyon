from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

email = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'

class N11bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.n11.com/")

        sleep(2)
        okay_button = self.driver.find_element_by_xpath('//*[@id="userKvkkModal"]/div/div[2]/span')
        okay_button.click()
        login_btn = self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/div[2]/div[2]/div/div/a[1]')
        login_btn.click()

        fb_btn = self.driver.find_element_by_xpath('//*[@id="loginContainer"]/div/div[1]/div/div[3]')
        fb_btn.click()

        #pop-up window
        sleep(2)
        popup = self.driver.window_handles[1]
        self.driver.switch_to.window(popup)
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)
        pw_in = self.driver.find_element_by_xpath('// *[ @ id = "pass"]')
        pw_in.send_keys(password)
        fb_login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login.click()

    def search(self):
        sleep(6)
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(base_window)
        search = self.driver.find_element_by_xpath('//*[@id="searchData"]')
        search.send_keys('samsung')
        search.send_keys()
        sleep(1)
        search_Btn = self.driver.find_element_by_xpath('//*[@id="header"]/div/div/div[2]/div[1]/a')
        search_Btn.click()
    def foundResult(self):
        sonuc = self.driver.find_element_by_xpath('//*[@id="contentListing"]/div/div/div[2]/section/div[1]/div[5]/strong')
        sonuc = int(sonuc)
        if sonuc > 0:
            self.driver.switch_to().alert().sendKeys(sonuc, "bulundu")
        else:
            self.driver.switch_to().alert().sendKeys("0", "sonuç bulundu")



bot = N11bot()
bot.login()
bot.search()



