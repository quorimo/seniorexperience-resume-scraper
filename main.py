from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import os 
import time
#######################################################
""" LOAD ENVIRONMENT VARIABLES """ 
load_dotenv()

email = os.environ.get('EMAIL') 
password = os.environ.get('PASSWORD')
download_dir = os.environ.get('RESUMES_DIR') 
chromedriver_dir = os.environ.get('CHROMEDRIVER_DIR') 

######################################################
""" OTHER SETUP STUFF """ 
s = Service(chromedriver_dir) 

chrome_options = Options()
chrome_options.add_argument("--headless") # you can see the window with this off   

prefs = {"download.default_directory": download_dir} 
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(service=s, options=chrome_options)

######################################################
""" OPEN PAGE AND LOGIN """ 

driver.get('https://www.bcaseniorexperience.org/login/') 

driver.find_element(By.ID, 'login-email').send_keys(email)
driver.find_element(By.ID, 'login-password').send_keys(password)

######################################################
""" OPEN PROFILE PAGES AND DOWNLOAD FILES """ 
counter = 0 

for i in range (1255, 1400): # these numbers are just from what i can tell, may not include all signed up students
  try:  
  # go to link
    driver.get('https://www.bcaseniorexperience.org/resume/' + str(i))
    
    # get student name 
    name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/h1').text
    name = name.replace(' ', '')

    # predownload
    before = os.listdir(download_dir) 
    
    # download
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div/ul/li[2]/a').click()
    time.sleep(0.5) # try testing different numbers  
    
    # renaming files 
    after = os.listdir(download_dir) 
    change = set(after) - set(before) 
    while(len(change)==0):
      pass
    if len(change)==1:
      latest_file = download_dir + change.pop() 
    a = latest_file.split(".")
    new_path = download_dir + name + "." +  a[len(a)-1]
    os.rename(latest_file, new_path)

  except:
    # yeah this logging thing is still not working correctly
    log = open("log.txt", "a") 
    log.write(str(i) + " doesn't exist or does not have a resume.\n") 
    log.close()

driver.quit()
print("DONE") 

