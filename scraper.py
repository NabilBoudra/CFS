from os import remove
import requests 
from bs4 import BeautifulSoup
from contestant import contestant
from plotter import plot 
problemRating = {}
username = "boredom" 
def getId(URL) : 
    tmp = URL.split('/')
    for x in tmp : 
        if x.isnumeric() : 
            return x+URL[-1]
    return 'Nan'
def toSeconds(timing) : 
    answer = int(timing[0:2])*60
    answer += int(timing[3:])
    return answer 
def getRating(link):     
    return int(problemRating[link])
if __name__ == "__main__" : 
    page = requests.get(f"https://codeforces.com/profile/{username}")
    res = str(page.content)
    contests = []
    with open('problemData.txt') as tmp : 
        lines = tmp.readlines()
        for line in lines : 
            URL = (line.split())[0]
            rating = (line.split())[1] 
            problemRating[URL]=rating 
    for i in range(0,len(res)-7): 
        if res[i:i+8] =="/contest" : 
            URL = "https://codeforces.com"
            for j in range(i,len(res)): 
                if res[j]=='"' : 
                    break 
                URL+=res[j]
            contests.append(URL)
    tmpcontest = []
    for contest in contests: 
        flg = 0
        for i in range(0,len(contest)-10):
            if contest[i:i+11]=="participant":
                flg = 1
        if flg : 
            tmpcontest.append(contest)
    contests = tmpcontest
    sumOfSpeeds = [-1 for i in range(30)]
    numberOfSolves = [0 for i in range(30)]
    for contest in contests : 
        page = requests.get(contest) 
        res = BeautifulSoup(page.content,'lxml')
        pId = ""
        flg=0
        for i in range(0,len(contest)) : 
            if flg and contest[i] != 'p' : 
                pId+=contest[i] 
            if contest[i]=='#':
                flg=1 
        tmp = res.find_all('tr',{'participantid':pId})
        row = tmp[0].find_all('td')
        del row[0:5]
        nProblems = len(row)
        firstRow = ((res.find_all('tr'))[0]).find_all('a')
        accepted = []
        for i in range(0,nProblems) : 
            spans = row[i].find_all('span') 
            if len(spans) == 2 : 
                accepted.append((toSeconds(spans[1].text),getId(firstRow[i].get('href'))))
        accepted = sorted(accepted) 
        last = 0
        for problem in accepted : 
            duration = problem[0]-last
            rating = getRating(problem[1])
            if rating != -1 : 
                sumOfSpeeds[rating]+=duration
                numberOfSolves[rating]+=1
            last=problem[0]
    average = [-1 for i in range(0,30)]
    for rating in range(0,30) : 
        if numberOfSolves[rating] : 
            average[rating] = sumOfSpeeds[rating]//numberOfSolves[rating]
    stats = contestant(username,average)
    if stats.valid() == False : 
        notEnoughData = True 
    else : 
        plot(stats.speed)