from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=3394117085&geoId=103121230&keywords=data%20mining').text
# put the link of the website you want to get data from
soup = BeautifulSoup(html_text, 'html5lib')
jobs = soup.find('li', class_ = 'ember-view   jobs-search-results__list-item occludable-update p0 relative scaffold-layout__list-item')
# for job in jobs:
company_name = jobs.find('a', class_ = 'disabled ember-view job-card-container__link job-card-list__title')



print(company_name)



