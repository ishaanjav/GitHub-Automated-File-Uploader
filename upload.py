'''
Created by ishaanjav
https://github.com/ishaanjav/GitHub-Automated-File-Uploader

=======================================================
SETUP Instructions
=======================================================
1. Line 14: Enter the repository link you want the automation tool to upload files to
2. Line 16: Enter GitHub username
3. Line 17: Enter GitHub password
-------------------------------------------------------
'''

repo_link = ""      # Example: https://github.com/ishaanjav/GitHub-Automated-File-Uploader
# Username and password to sign into GitHub.
email = "" 
passw = ""

import time
import selenium
from time import sleep
from selenium import webdriver
import sys, os
import requests
from datetime import datetime
from datetime import date
import os.path, operator

from contextlib import contextmanager
from webdriver_manager.chrome import ChromeDriverManager


# Code to open the browser (Google Chrome
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stderr
        sys.stderr = devnull
        try:  
            yield
        finally:
            sys.stderr = old_stdout

dir = sys.argv[1]

browser = None
with suppress_stdout():
    browser = webdriver.Chrome(ChromeDriverManager().install()) # Will install latest version or used cached version if already present.
    print ("\033[A                             \033[A")


# Function to sign into the GitHub account and go to the repository
def signin():
    browser.get("https://github.com/login")
    login = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[1]")
    password = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[2]")
    login.send_keys(email)
    password.send_keys(passw)

    signin_btn = browser.find_element_by_xpath("/html/body/div[3]/main/div/form/div[4]/input[12]")
    signin_btn.click()
    browser.get(repo_link)

# Function to upload a file to GitHub given the filename and the file's contents.
def create_files(file_name, file_contents):
    browser.get(repo_link+"/new/main")
    name = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/form[2]/div/div[1]/span/input")
    box = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/form[2]/div/div[5]/div[2]/div/div[5]/div[1]/div/div/div/div[5]/div/pre/span")
    commit = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/form[2]/div/div[6]/button")
    name.send_keys(file_name)
    box.send_keys(file_contents)
    commit.click()

# Check if a file is already in the GitHub repo. Returns a boolean (true or false)
def already_exists(file_name):
    return (("\"" + file_name + "\"") in browser.page_source)


# call the sign in function
signin()

# Upload all files in directory (dir is the directory variable)
if sys.argv[2] == "":
    for file in os.listdir(dir):
        if already_exists(file): 
            print("Skipping: " + str(file))
            continue
        f = open(str(dir) +"/"+file, "r")
        print("Uploading: " + str(file))
        create_files(file, str(f.read()))
# upload the files provided in the sys.argv array       
else:
    for file in sys.argv[2:]:
        if len(file) < 1 or file == "":
            continue
        if already_exists(file):
            print("Skipping: " + str(file))
            continue

        f = open(str(dir) + "/" + file, "r")
        print("Uploading: " + str(file))
        create_files(file, str(f.read()))


# Print done and close the browser after 8 seconds
print("Done!")
sleep(8)
browser.close()


