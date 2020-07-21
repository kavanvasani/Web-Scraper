import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

links = soup.select('.storylink')
links2 = soup2.select('.storylink')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

megalinks = links + links2
megasubtext = subtext + subtext2

def sort_by_votes(news_list):
	return sorted(news_list,key = lambda k:k['votes'],reverse = True)

def create_custom(links,subtext):
	news = []
	for index,item in enumerate(links):
		title = links[index].getText()
		href = links[index].get('href', None)
		vote = subtext[index].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			if points > 99:
				news.append({'title' : title, 'href':href ,'votes':points})
	return sort_by_votes(news)


pprint.pprint(create_custom(megalinks,megasubtext))