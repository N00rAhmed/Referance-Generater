import sys
import requests
from bs4 import BeautifulSoup
from datetime import date
import time

def main():
    header = input('Header: ')
    published_year = input('Published year of web page: ')
    url = input('URL: ')

    reqs = requests.get(url)

    # Gets current date
    today = date.today()

    # Formats current date as a string in the "day/month/year" format
    access_date = today.strftime("%d/%m/%Y")

    soup = BeautifulSoup(reqs.text, 'html.parser')

    for title in soup.find_all('title'):
        ref = header + f' ({published_year}) ' + (title.get_text() + ' [online]' + ' Address: ' + url + f' [accessed: {access_date}] ')
        with open('Database.txt', 'a') as file:
            storage = file.write(str(ref) + '\n')

    pull_data = input('Type pull to see all your references, if not then press enter: ')
    if pull_data == 'pull':
        with open('Database.txt') as f:
            contents = f.read()
            print(contents)
            print("_______________________________________________________________________________________________________________")
            time.sleep(5)
    else:
        print('Bye')
        sys.exit()
        

if __name__ == "__main__":
    main()
