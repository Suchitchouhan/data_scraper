import requests
from bs4 import BeautifulSoup
import pandas as pd
result="contractsfinder"
data_list=[]
for x in range(1,113):
    URL = f"https://www.contractsfinder.service.gov.uk/Search/Results?page={x}"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'}
    page=requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    result_btl=soup.find("body").find_all("table")
    result_btl=soup.find_all("div",class_="search-result")
    for x in result_btl:
        empty_dict={}
        empty_dict['title']=x.find("a").text
        empty_dict['subheader']=x.find("div",class_="search-result-sub-header").text
        empty_dict['description']=x.find_all("div",class_="wrap-text")[1].find("span")
        print(empty_dict['title'])
        for x in x.find_all("div",class_="search-result-entry"):
            empty_dict[x.find("strong").text]=x.text.replace(x.find("strong").text,"")
        data_list.append(empty_dict)

df = pd.DataFrame.from_dict(data_list) 
df.to_csv("data.csv")

