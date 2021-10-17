from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.instagram.com/')

#login_link = browser.find_element_by_xpath("//a[text()='Log in']")
#login_link.click()
name = input("Enter your username: ")
passW = input("Enter your password: ")
class InstaBot():
    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord

    def login(self):
        driver.get("https://www.instagram.com")

        User = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        User.send_keys(self.userName)

        Pass = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        Pass.send_keys(self.passWord)
hello=InstaBot(name,passW)
hello.login()

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()



