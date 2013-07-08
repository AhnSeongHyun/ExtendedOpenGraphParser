# -*- coding: utf-8 -*-
 
import opengraph
import re
import urllib2 



def parse(url):
	parseResult = {}
	ogpResult = opengraph.OpenGraph(url=url)
	 

	if ogpResult.is_valid() == True:
		pass
		#통과를 해도 title, image, url 이 없으면 해당의 것을 찾아야 한다.  
	else:
		parseResult = parseNonVaildUrl(url, parseResult)



	return parseResult; 


def parseNonVaildUrl(url, parseResult):

	#url 에서 html 을 가져온다. 
	html = getHtml(url)
	#html 에서 title을 가져온다. 
	parseResult['title'] = getTitle(html)

	#첫번째 이미지를 가져온다. 
	parseResult['image'] = getPresentImage(url)

	#url을 가져온다.  
	parseResult['url'] = getUrl(url)
	return parseResult; 

def getPresentImage(url):
	return None


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
	#url = "http://www.youtube.com/watch?v=q3ixBmDzylQ"
	#print(parse(url)) 

	url = "http://ash84.tistory.com"
	print(parse(url))