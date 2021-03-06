from urllib.request import urlopen
from bs4 import BeautifulSoup
from WebD import Data

#mother_link="https://github.com/maifeeulasad/Desktop-File-Organizer/tree/master/DiskOrganizer/Properties"
mother_link="https://www.facebook.com/"

visited=[]

mother={}

def go_to(link):
    print(link)
    if link not in visited and link.startswith(mother_link):
        visited.insert(0,link)
        quote_page = link
        try:
            page = urlopen(quote_page)
            soup = BeautifulSoup(page, 'html.parser')
            tem =[]
            for a in soup.find_all('a', href=True):
                ins=a['href']
                if not ins.startswith("#") or not ins.startswith(" "):
                    if ins.startswith('?'):
                        ins=mother_link+ins
                    elif ins.startswith("/"):
                        ins=mother_link[:-1]+ins
                    tem.insert(0,ins)
                if ins.startswith(mother_link):
                    go_to(ins)
                    mother[ins] = tem
        except:
            print("error")
            #pass


go_to(mother_link)

Data.mo=mother_link

Data.links=mother


Data.get_links_as_list()
Data.visualize()