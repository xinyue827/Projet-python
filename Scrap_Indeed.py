#!/usr/bin/env python
# coding: utf-8

# #  Indeed crawler and data selection

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

cService = webdriver.ChromeService(executable_path=r'C:\Users\JIANG JING JING\Downloads\chromedriver-win64\chromedriver.exe')

def scrape_job_links(keywords, num_pages):
    links = []
    driver = webdriver.Chrome(service=cService) 
    
    for keyword in keywords:
        for page in range(1, num_pages + 1):
            start = page * 10
            url = f"https://fr.indeed.com/emplois?q={keyword}&l=%C3%8Ele-de-France&sc=0kf%3Ajt(apprenticeship)%3B&start={start}"
            driver.get(url)
            time.sleep(4)

            my_range = [i for i in range(1, 18)]
            for i in my_range:
                xpath_expression = '/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li[{}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[1]/h2/a'.format(i)
                elements = driver.find_elements(By.XPATH, xpath_expression)
                if not elements:
                    continue
                link = elements[0].get_attribute('href')
                links.append(link)
    
    driver.quit()
    return links

scrape_job_links(['data analyst'], 15)
  
len(links)

def found_emails(links):
    found_emails = []
    driver = webdriver.Chrome() 
    
    try:
        for link in links:
            driver.get(link)
            content = driver.page_source 
            soup = BeautifulSoup(content, 'html.parser')
            job_description_element = soup.find('div', id='jobDescriptionText')

            if job_description_element is not None:
                job_description = job_description_element.get_text()
                email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                emails = re.findall(email_pattern, job_description)
                if emails:
                    for email in emails:
                        found_emails.append((email, link))
                time.sleep(2)
    finally:
        driver.quit()  

    return found_emails

found_emails_result = found_emails(scrape_job_links(['data', 'analyst'], 15))
print(found_emails_result)



def filter_emails_rh(emails_found):
    filtered_emails = [(email, link) for email, link in emails_found if re.search(r'rh|recrutement|hr', email.lower())]
    return filtered_emails

filtered_emails_rh = filter_emails_rh(found_emails_result)
print(filtered_emails_rh)


def scrape_job_descriptions(filtered_emails_rh):
    job = {}
    driver = webdriver.Chrome()
    
    try:
        for email, link in filtered_emails_rh:  
            driver.get(link)
            content = driver.page_source 
            soup = BeautifulSoup(content, 'html.parser')
            job_description = soup.find('div', id='jobDescriptionText')
            if job_description:
                job[email] = job_description.text
    finally:
        driver.quit()
    
    return job

def print_job_descriptions(job):
    for email, description in job.items():
        print(f"Email: {email}\nDescription: {description}\n")

job = scrape_job_descriptions(filtered_emails_rh)
print_job_descriptions(job)



import pandas as pd
def export_to_excel(job, excel_filename):
    df = pd.DataFrame(list(job.items()), columns=['Email', 'Description'])
    df.to_excel('job_descriptions.xlsx', index=False)
job = scrape_job_descriptions(filtered_emails_rh)
export_to_excel(job, 'job_descriptions.xlsx')
import os
print(os.getcwd())

