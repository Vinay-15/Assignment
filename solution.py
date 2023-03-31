from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
path = 'chromedriver/chromedriver'

driver = webdriver.Chrome(path)
driver.get(url)
time.sleep(5)

x = driver.find_elements(By.TAG_NAME,'tr')[3:-1]  # extracting all the data on the main page
ques_no = []
if len(x)>10:
    x = x[:10]
for i in x:
    ele = i.text.replace('\n',' ').split(' ')  # collecting quest number from the data
    ques_no.append(ele[1])
print('------------------------------------------------------------------------------------------------------')

for i in ques_no:  # to access each new page
    print('Quest Number:',i)
    button = driver.find_element(By.XPATH,f'//a[@onclick="prevnext({i}); return false;"]')  # using quest no. as a button to open the link
    button.click()
    time.sleep(5)
    data = driver.find_elements(By.TAG_NAME,'td')    # to extract all data in new page results
    l = []
    for j in data[:-1]:
        d = j.text.strip()
        if d!='':
            l.append(d)
    count = 0
    for z in range(len(l)):
        if l[z] == 'Closing Date:' or l[z] == 'Est. Value Notes:' or l[z] == 'Description:':
            print(l[z], l[z + 1])
            count += 1
            if count == 3:
                break
    print('------------------------------------------------------------------------------------------------------')
    ex_button = driver.find_element(By.XPATH,'//a[@href="/cdn/posting/?group=1950787&provider=1950787"]')
    ex_button.click()
    time.sleep(5)
driver.quit()