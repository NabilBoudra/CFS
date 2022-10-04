import sys 
import requests 
import scraper 
import time 
import contestant 
from bs4 import BeautifulSoup
import lxml
page = BeautifulSoup(requests.get('https://codeforces.com/').content,'lxml')
with open('problemData.txt','w') as oFile : 
    for pageIndex in range(1,1000000): 
        npage = BeautifulSoup(requests.get(f'https://codeforces.com/problemset/page/{pageIndex}').content,'lxml')
        if page == npage : 
            break 
        rows = npage.find_all('tr')
        del rows[0]
        for row in rows : 
            cell = row.find_all('td') 
            if len(cell) == 0: 
                continue 
            tmp = cell[3].find('span')
            if str(tmp) == "None": 
                continue 
            URL =  scraper.getId((cell[0].a)['href'])
            rating = contestant.convertToPractical(int((cell[3].span).text))
            oFile.write(URL+" "+str(rating)+'\n') 
        page = npage 