# seniorexperience-resume-scraper

### documentation 

This is a very simple script. You'll need Selenium and python-dotenv. And chromedriver.    
Inside the directory, make a folder to store the downloaded files. Also create a log.txt. 

In your .env file:
```
EMAIL='johndoe@gmail.com'
PASSWORD='dohnjoe'
RESUMES_DIR='/Users/johndoe/projects/thisproject/downloaded_files'
CHROMEDRIVER_DIR='/usr/local/bin/chromedriver'
```
RESUMES_DIR should be the path to your downloaded files folder. CHROMEDRIVER_DIR is the path to chromedriver. On MacOS, it's probably the one I provided. 

Note that currently the logging system does not work. 

Just run main.py!
