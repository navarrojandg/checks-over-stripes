import random
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config import config


class NikeAccount():
    # _name is a tuple with (first,last)
    # _dob is a tuple with (month,day,year)
    def __init__(self, _name, _dob, _id, _proxy=None):
        self.name = _name
        self.dob = _dob
        self.email = '{}{}{}@{}'.format(self.name[0],self.name[1],self.dob[random.choice([0,1,2])],config["domain"])
        self.password = config["password"]
        self.id = _id
        self.proxy = _proxy
        self.driver = None
        self.created = False

    def create(self):
        try:
            # options should go here
            chrome_ops = webdriver.ChromeOptions()
            if self.proxy != None:  
                chrome_ops.add_argument('--proxy-server={}'.format(self.proxy))
            chrome_ops.add_argument("--window-size=600,600")

            # use selenium to create account
            self.driver = webdriver.Chrome(chrome_options = chrome_ops)

            # edit so that you can support multiple regions
            self.driver.get(config["registerURL"]["US"])

            # we wait for create button to show
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//form/div/input[@type="button"]')))

            create_account_button = self.driver.find_element_by_xpath('//form/div/input[@type="button"]')
            invalid_input_xpath = '//form/div[contains(@class," invalid")]/input'
            invalid_gender_xpath = '//form/div[contains(@class," invalid")]/ul/li'

            # we trigger this in order to get the proper form elements to fill
            create_account_button.click()

            # build a list of correct inputs to fill 
            input_list = self.driver.find_elements_by_xpath(invalid_input_xpath)

            # select random gender
            gender_list = self.driver.find_elements_by_xpath(invalid_gender_xpath)
            random.choice(gender_list).click()

            #fill out the inputs
            for i in range(len(input_list)):
                if i == 0:
                    #email
                    input_list[i].send_keys(self.email)
                if i == 1:
                    #password
                    input_list[i].send_keys(self.password)
                    continue
                if i == 2:
                    #first name
                    input_list[i].send_keys(self.name[0])
                    continue
                if i == 3:
                    #last name
                    input_list[i].send_keys(self.name[1])
                    continue
                if i == 4:
                    #dob
                    # input_list[i].send_keys('{}/{}/{}'.format(self.dob[0], self.dob[1], self.dob[2]))
                    input_list[i].send_keys(self.dob[0])
                    input_list[i].send_keys(self.dob[1])
                    input_list[i].send_keys(self.dob[2])
                    continue
                if i == 5:
                    continue

            # submit form
            create_account_button.click()

            # wait until continue button shows up, that means successful sign up
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="accountStandalone"]/div/div/div[2]/div/div/div[1]/button')))
            self.created = True

        except:
            pass
        finally:
            self.driver.close()     

    def export(self):
        return '{}:{}'.format(self.email,self.password)

