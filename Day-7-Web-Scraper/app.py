from requests import get
from bs4 import BeautifulSoup
import csv

# Repositories listed on page = 1, it scrapes only the public repos.
# I have 53 repos in total. 30 repos and 18 repos are in page=1 and  are in page=2 respectively 
# which means 5 remaining repos are private. 48 repos are public
response = get("https://github.com/fojanb?page=1&tab=repositories")
if response.status_code == 200:
    final_data = []
    # print(response.text)
    my_soup = BeautifulSoup(response.text,'html.parser')
    all_repo_titles = my_soup.select('h3.wb-break-all a')
    print(all_repo_titles)
    for title in all_repo_titles:
        final_data.append(title.text)

filename = 'github_reops.csv'
header = ["Repo Name"]
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    for item in final_data:
        csvwriter.writerows(item) # 5. write the rest of the data

# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/