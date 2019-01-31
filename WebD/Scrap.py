from urllib.request import urlopen
from bs4 import BeautifulSoup

mother_link="http://codeforces.com"

mother={}

def go_to(link):
    if link not in mother:
        quote_page = link
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        tem =[]
        for a in soup.find_all('a', href=True):
            ins=a['href']
            if ins!="#":
                if ins.startswith("/") or ins.startswith("?"):
                    tem.insert(0,mother_link+ins)
                else:
                    tem.insert(0,ins)
        return tem


mother[mother_link] = go_to(mother_link)


print("-----------------------------")

for xx in mother:
    print(xx)
    for yy in mother[xx]:
        print("---"+yy)



