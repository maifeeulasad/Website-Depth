from urllib.request import urlopen
from bs4 import BeautifulSoup

mother_link="http://codeforces.com"

visited=[]

mother={}

def go_to(link):
    print(link)
    if link not in visited:
        visited.insert(0,link)
        quote_page = link
        print("visited sites --- ")
        print(visited)
        page = urlopen(quote_page)
        soup = BeautifulSoup(page, 'html.parser')
        tem =[]
        for a in soup.find_all('a', href=True):
            ins=a['href']
            if ins!='#':
                if ins.startswith("/") or ins.startswith('?'):
                    ins=mother_link+ins
                tem.insert(0,ins)
                print('---'+ins)
            if ins.startswith(mother_link):
                go_to(ins)
        mother[ins] = tem





go_to(mother_link)



'''


print("-----------------------------")

for xx in mother:
    print(xx)
    for yy in mother[xx]:
        print("---"+yy)





'''
