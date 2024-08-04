from selenium import webdriver
import time

web = webdriver.Chrome()
web.get("strona")
time.sleep(2)

firstName = "Mateusz"
lastName = "Gomulinski"
emailAdd = "mateuszg943@gmail.com"
subjectTxt = "Test"
messageTxt = "Test"

first = web.find_element("xpath", '//*[@id="wpforms-83-field_0"]')
first.send_keys(firstName)

last = web.find_element("xpath", '//*[@id="wpforms-83-field_0-last"]')
last.send_keys(lastName)

email = web.find_element("xpath", '//*[@id="wpforms-83-field_3"]')
email.send_keys(emailAdd)

subject = web.find_element("xpath", '//*[@id="wpforms-83-field_4"]')
subject.send_keys(subjectTxt)

message = web.find_element("xpath", '//*[@id="wpforms-83-field_2"]')
message.send_keys(messageTxt)

rodo = web.find_element("xpath", '//*[@id="wpforms-83-field_5_1"]')
rodo.click()

submit = web.find_element("xpath","//button[@type='submit']")
submit.click()
