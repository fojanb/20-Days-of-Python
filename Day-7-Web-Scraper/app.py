from requests import get
from bs4 import BeautifulSoup


response = get("https://github.com/fojanb?tab=repositories")
# print(response.text)
my_soup = BeautifulSoup(response.text,'html.parser')
print(my_soup.title)
