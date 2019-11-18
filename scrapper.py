"""
requirements 
install python 
pip install selenium
download gechodriver for firefox or chrome driver for googlechorome and add the file location to env PATH variable
"""


from selenium import webdriver

def login(url,uname,pswd):
    browser=webdriver.Chrome()  #or webdriver.Firefox()
    browser.get(url)
    browser.implicitly_wait(10)
    username=browser.find_element_by_id("okta-signin-username")
    browser.implicitly_wait(10)
    password=browser.find_element_by_name('password')
    username.clear()
    password.clear()    
    username.send_keys(uname)
    password.send_keys(pswd)   
    browser.implicitly_wait(10)
    submitbtn=browser.find_element_by_id('okta-signin-submit')
    submitbtn.click()        
    browser.implicitly_wait(100)
    gcode=browser.find_element_by_id('input10')
    gcode.clear()  
    gcode.send_keys(426081) #pass otp
    gcode.send_keys('\n')

login(
)
