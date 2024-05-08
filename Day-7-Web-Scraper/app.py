from requests import get
from bs4 import BeautifulSoup

# Repositories listed on page = 1, it scrapes only the public repos.
# I have 53 repos in total. 30 repos and 18 repos are in page=1 and  are in page=2 respectively 
# which means 5 remaining repos are private. 48 repos are public
response = get("https://github.com/fojanb?page=1&tab=repositories")
# print(response.text)
my_soup = BeautifulSoup(response.text,'html.parser')
all_repo_titles = my_soup.select('h3.wb-break-all a')
for title in all_repo_titles:
    print(f"{title.text}")
