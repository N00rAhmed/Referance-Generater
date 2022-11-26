import sys
import requests
from bs4 import BeautifulSoup
from datetime import date
# https://www.forbes.com/sites/christinemoorman/2018/01/12/why-apple-is-still-a-great-marketer-and-what-you-can-learn/?sh=748f802515bd
# https://www.simplilearn.com/tutorials/marketing-case-studies-tutorial/tesla-marketing-strategy

header = input('Header: ')

published_year = input('Published year of web page: ')

url = input('URL: ')
reqs = requests.get(url)

today = date.today()
# dd/mm/YY
access_date = today.strftime("%d/%m/%Y")

soup = BeautifulSoup(reqs.text, 'html.parser')

# instead of function create while loop or for loop to keep iterating same program
for title in soup.find_all('title'):
    ref =  header + f' ({published_year}) ' + (title.get_text() + ' [online]' + ' Address: ' + url + f' [accessed: {access_date}] ')

    # print(ref)

    file = open('Database.txt', 'a')
    storage = file.write(str(ref) + '\n')

    file.close()

    pull_data = input('Type pull to see all your references, if not then press enter: ')
    if pull_data == 'pull':
        with open('Database.txt') as f:
            contents = f.read()
            print(contents)
    else:
        ('Bye')
        sys.exit()