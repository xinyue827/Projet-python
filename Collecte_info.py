# # collecte d'informations sur les offres d'emploi

#  Liens sur l'emploi  
cService = webdriver.ChromeService(executable_path=r'C:\Users\JIANG JING JING\Downloads\chromedriver-win64\chromedriver.exe')

def job_links(domains, num_pages):
    links = []
    driver = webdriver.Chrome(service=cService) 
    
    for domain in domains:
        for page in range(1, num_pages + 1):
            start = page * 10
            url = f"https://fr.indeed.com/emplois?q={domain}&l=%C3%8Ele-de-France&sc=0kf%3Ajt(apprenticeship)%3B&start={start}"
            driver.get(url)
            time.sleep(4)

            for i in range(1,18):
                xpath_expression = '/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li[{}]/div/div[1]/div/div/div/table[1]/tbody/tr/td/div[1]/h2/a'.format(i)
                elements = driver.find_elements(By.XPATH, xpath_expression)
                if not elements:
                    continue
                link = elements[0].get_attribute('href')
                links.append(link)
    
    driver.quit()
    return links

# Nombres des emplois
links = job_links(['data','analyst'], 15)
len(links)


# # Chercher les mails des emplois

# Affiche des liens vers les offres d'emploi de toutes les entreprises et les courriels correspondants
def find_emails(links):
  emails_found = []
  driver = webdriver.Chrome(service=cService) 
  for link in links:
      driver.get(link)
      content = driver.page_source 
      soup = BeautifulSoup(content, 'html.parser')
      job_description_element = soup.find('div', id='jobDescriptionText')

      if job_description_element is not None:
          job_description = job_description_element.get_text()
          time.sleep(2)
          email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
          emails = re.findall(email_pattern, job_description)
          
          if emails:
              for email in emails:
                  emails_found.append((email, link))
                  
  driver.quit()  
  return emails_found

#  La sélection ne porte que sur les boîtes aux lettres avec hr ou recrutement.
emails_found = find_emails(links)
emails_rh = [(email, link) for email, link in emails_found if re.search(r'rh|recrutement|hr', email.lower())]
print(emails_rh)


# # Descriptions des emplois
def job_descriptions(email_link):
    job = {}
    driver = webdriver.Chrome(service=cService)
    
    for email, link in email_link:  
        driver.get(link)
        content = driver.page_source 
        soup = BeautifulSoup(content, 'html.parser')
        job_description = soup.find('div', id='jobDescriptionText')
        if job_description:
            job[email] = job_description.text

    driver.quit()
    return job
  
job_description = job_descriptions(emails_rh)


# # Expoter les informations

df = pd.DataFrame(list(job_description.items()), columns=['Email', 'Description'])
result = df.to_excel('job_descriptions.xlsx', index=False)

os.getcwd() # pour voir où est le fichier excel

