# -*- coding: utf-8 -*-
 
import opengraph
import re
import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup



def parse(url=None,html=None):
	parseResult = {}

	if url is None and html is not None:
		parseResult = parseHtml(html)

	elif url is not None:
		parseResult = parseUrl(url)
	else:
		raise Exception("url and html are None.")
 
	return parseResult

def parseHtml(html):
	parseResult ={}
	ogpResult = opengraph.OpenGraph(html=html)
	
	if ogpResult.is_valid() is True:
		parseResult = pasrseValidHtml(html,ogpResult)

	else :
		parseResult = parseNonValidHtml(html)
	return parseResult


def pasrseValidHtml(html, ogpResult):
	parseResult ={}

	for key in ogpResult.keys():
		parseResult[key] = ogpResult[key];

	#_url은 뺀다. 
	if parseResult.has_key("_url") is True:
		parseResult.pop("_url", None)

	#required 요소가 없으면 가져와야 한다. 
	if parseResult.has_key('url') is False:
		parseResult['url'] = getUrl(html=html)
		
	if parseResult.has_key('image') is False:
		parseResult['image'] = getMainImage(html);

	if parseResult.has_key('title') is False:
		parseResult['title'] = getTitle(html);

	if parseResult.has_key('type') is False:
		parseResult['type'] = getType(html=html)

	return parseResult;

 


def parseNonValidHtml(html):
	parseResult = {}

	parseResult['title'] = getTitle(html)
	parseResult['image'] = getMainImage(html)
	parseResult['url'] = getUrl(html=html)
	parseResult['type'] = getType(html=html)

	return parseResult; 


def parseUrl(url):
	parseResult ={}
	ogpResult = opengraph.OpenGraph(url=url)

	if ogpResult.is_valid() == True:		
		parseResult = parseValidUrl(url, ogpResult)
	else:
		parseResult = parseNonVaildUrl(url) 

	return parseResult; 


def parseValidUrl(url, ogpResult):

	parseResult ={}

	for key in ogpResult.keys():
		parseResult[key] = ogpResult[key];

	#_url은 뺀다. 
	if parseResult.has_key("_url") is True:
		parseResult.pop("_url", None)

	html = getHtml(url);

	#required 요소가 없으면 가져와야 한다.
	if parseResult.has_key('url') is False:
		parseResult['url'] = getUrl(url=url)
		
	if parseResult.has_key('image') is False:
		parseResult['image'] = getMainImage(html);

	if parseResult.has_key('title') is False:
		parseResult['title'] = getTitle(html);

	if parseResult.has_key('type') is False:
		parseResult['type'] = getType(url=url)

	return parseResult

def parseNonVaildUrl(url):

	#getHtml from url 
	parseResult = {}
	html = getHtml(url)

	parseResult['title'] = getTitle(html)
	parseResult['image'] = getMainImage(html)
	parseResult['url'] = getUrl(url)
	parseResult['type'] = getType(html)

	return parseResult; 

 

def getMainImage(html):

	mainImage =""
	soup = BeautifulSoup(html)
	images = soup.html.find_all('img')
	
	for image in images: 
		if image.has_attr('src') is True:
			if '.gif' not in image['src']:
				mainImage = image['src'] #first image

	return mainImage


def getUrl(url=None, html=None):

	if url is not None:
		  
		lastIdx = url.rfind("/")
		if url[lastIdx-1] == "/":# it is http://
			return url 
		else:
			return url[:lastIdx]
	else:
		return None

def getType(url=None, html=None):
	#default 'website'
	return 'website'

def getTitle(html):

	title=""
	soup = BeautifulSoup(html)  
	return soup.html.head.title.contents[0]

def getHtml(url):
	raw = urllib2.urlopen(url)
	html = raw.read() 
	return html

 