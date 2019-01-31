from urllib.request import urlopen
from bs4 import BeautifulSoup

mother_link="https://github.com/maifeeulasad"

visited=[]

mother={}

def go_to(link):
    print(link+"-ok")
    if link not in visited and link.startswith(mother_link):
        visited.insert(0,link)
        quote_page = link
        try:
            page = urlopen(quote_page)
            soup = BeautifulSoup(page, 'html.parser')
            tem =[]
            for a in soup.find_all('a', href=True):
                ins=a['href']
                if ins!='#' or ins!='' or ins.isspace()!=True:
                    if ins.startswith("/") or ins.startswith('?'):
                        ins=mother_link+ins
                    tem.insert(0,ins)
                if ins.startswith(mother_link):
                    go_to(ins)
                    mother[ins] = tem
        except:
            print("error")

go_to(mother_link)


'''

for xx in mother:
    print("************************")
    print(xx+"-me")
    print("************************")
    for yy in mother[xx]:
        print("---"+yy)




'''
