# -*- coding: utf-8 -*-
 
import opengraph
import re
import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


def parse(url):
	parseResult = {}
	ogpResult = opengraph.OpenGraph(url=url)
	 

	if ogpResult.is_valid() == True:
		
		if ogpResult['_url'] is not None:
			parseResult['url'] = ogpResult['_url']
		
		if ogpResult['image'] is not None:
			parseResult['image'] = ogpResult['image']
		 
		if ogpResult['title'] is not None:
			parseResult['title'] = ogpResult['title']

		if ogpResult['type'] is not None:
			parseResult['type'] = ogpResult['type']
		

	else:
		parseResult = parseNonVaildUrl(url, parseResult)



	return parseResult; 


def parseNonVaildUrl(url, parseResult):

	#url 에서 html 을 가져온다. 
	html = getHtml(url)
	#html 에서 title을 가져온다. 
	parseResult['title'] = getTitle(html)

	#첫번째 이미지를 가져온다. 
	parseResult['image'] = getPresentImage(html)

	#url을 가져온다.  
	parseResult['url'] = getUrl(url)

	#type을 가져온다. 
	parseResult['type'] = getType(html)

	return parseResult; 


def getType(html):
	return None

def getPresentImage(html):

	presntImage =""
	soup = BeautifulSoup(html)
	images = soup.html.find_all('img')
	
	for image in images: 
		if '.gif' not in image['src']:
			presntImage = image['src'] #first image

	return presntImage


def getUrl(url):
	return url

def getTitle(html):

	title=""
	linebyhtml = html.split("\n")
	for line in linebyhtml:
		if "<title>" in line:
			st= line.find('>')
			ed= line.rfind('<')
			title = line[st+1:ed]
			break 
	return title


def getHtml(url):
	raw = urllib2.urlopen(url)
	html = raw.read() 
	return html


if __name__ == '__main__':
	
	print "youytube"
	url1 = "http://www.youtube.com/watch?v=q3ixBmDzylQ"
	print(parse(url1)) 

	print "tistory"
	url2 = "http://indf.tistory.com/"
	print(parse(url2))