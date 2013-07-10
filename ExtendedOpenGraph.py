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
	# TODO : Implementation
	pass

def parseUrl(url):
	parseResult ={}
	ogpResult = opengraph.OpenGraph(url=url)

	if ogpResult.is_valid() == True:
		
		if ogpResult['_url'] is not None:
			parseResult['url'] = ogpResult['_url']
		
		if ogpResult['image'] is not None:
			parseResult['image'] = ogpResult['image']
		else:
			# TODO : getMainImage(url)
		 
		if ogpResult['title'] is not None:
			parseResult['title'] = ogpResult['title']
		else:
			# TODO : getTitle(url)

		if ogpResult['type'] is not None:
			parseResult['type'] = ogpResult['type']
	else:
		parseResult = parseNonVaildUrl(url, parseResult) 

	return parseResult; 


def parseNonVaildUrl(url, parseResult):

	#getHtml from url 
	html = getHtml(url)

	parseResult['title'] = getTitle(html)
	parseResult['image'] = getMainImage(html)
	parseResult['url'] = getUrl(url)
	parseResult['type'] = getType(html)

	return parseResult; 


def getType(html):
	return None

def getMainImage(html):

	mainImage =""
	soup = BeautifulSoup(html)
	images = soup.html.find_all('img')
	
	for image in images: 
		if '.gif' not in image['src']:
			mainImage = image['src'] #first image

	return mainImage


def getUrl(url):
	return url

def getType(url):
	#default 'website'
	return 'website'

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

 