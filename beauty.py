import sys

import requests
from bs4 import BeautifulSoup


def load_user_data(page, session):
    request = session.get(page)
    return request.text


# establishing session
s = requests.Session()

s.headers.update({
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
})

page_url = sys.argv[1]

# loading files
data = load_user_data(page_url, s)
soup = BeautifulSoup(data, "lxml")
found_tags = soup.find_all(attrs={"style": True})
for l in found_tags:
    del (l["style"])

print(soup.prettify(), end='\n')
input("Press Enter to continue")
