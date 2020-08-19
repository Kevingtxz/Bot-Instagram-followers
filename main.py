from selenium import webdriver
from time import sleep
from pandas import read_excel

list_accounts = read_excel(r"C:\Users\Developer\Desktop\Bot Instagram followers\lista_de_contas.xlsx")
list_to_follow = read_excel(r"C:\Users\Developer\Desktop\Bot Instagram followers\lista_para_seguir.xlsx")
count = 0
while(isinstance(list_accounts['Email'][count], str)):
    class InstaBot:
        def __init__(self, username, pw):
            self.driver = webdriver.Firefox()
            self.username = username    
            self.driver.get('https://www.instagram.com/?hl=es-es')
            sleep(2)
            self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
                .send_keys(username)
            self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
                .send_keys(password)
            self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            sleep(4)
            # self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            # sleep(3)

        def follow_it(self, links_profiles):
            # num is the second count
            num = 1
            while(isinstance(list_to_follow['Link'][num], str)):
                sleep(3)
                self.driver.get(list_to_follow['Link'][num])
                sleep(2)
                self.driver.find_element_by_xpath("//button[contains(text(), 'Seguir')]").click()
                sleep(4)
                num += 1
            self.driver.find_element_by_xpath
            self.driver.close()

    username = list_accounts['Email'][count]
    password = list_accounts['Senha'][count]

    my_bot = InstaBot(username, password)
    my_bot.follow_it(list_to_follow['Link'][count])
    count += 1