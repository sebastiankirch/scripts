import click
from bs4 import BeautifulSoup
import urllib2
import re
import codecs

def parseWebsites():
	assetIdsFile = codecs.open('D:/assetids.txt', 'w', 'utf-8')
	urlsFile = codecs.open('D:/urls.txt', 'w', 'utf-8')	

	page = urllib2.urlopen('file:///D:/berlin-mauer.html')
	parsed = BeautifulSoup(page)
	links = parsed.findAll('a',title='Video ansehen')
	for link in links:
		url = 'http://www.berlin-mauer.de' + link.get('href')
		html_page = urllib2.urlopen(url)
		soup = BeautifulSoup(html_page)
		ul = soup.findAll('ul',class_='versions')
		li = ul[0].findChildren(recursive=False)
		a = li[1].findChildren(recursive=False)
		link =  a[0].get('href')

		i = link.replace('.mp4','').replace('http://http-stream.rbb-online.de/rbb/projekte/mauerfall/','')

		titles = soup.findAll('h1',itemprop='name')
		title =  titles[0].contents[0]

		assetIdsFile.write(i + ";" + title + "\n")
		urlsFile.write(link + "\n")

	assetIdsFile.close()
	urlsFile.close()

if __name__ == '__main__':
    parseWebsites()