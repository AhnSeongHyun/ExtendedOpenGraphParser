# -*- coding: utf-8 -*-


# encoding: utf-8

import unittest
import ExtendedOpenGraph



HTML = """
<html xmlns:og="http://ogp.me/ns#">
<head>
<title>The Rock (1996)</title>
<meta property="og:title" content="The Rock" />
<meta property="og:type" content="movie" />
<meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
<meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
</head>
</html>
"""


class test(unittest.TestCase):

    def test_html(self):
    	data = ExtendedOpenGraph.parse(html=HTML)

    def test_valid_url(self):
    	URL = "http://www.youtube.com/watch?v=q3ixBmDzylQ"
    	data = ExtendedOpenGraph.parse(url=URL)
    	print data
    	
    	self.assertEqual(data['title'],'While My Guitar Gently Weeps')
    	self.assertEqual(data['image'] ,'http://i1.ytimg.com/vi/q3ixBmDzylQ/hqdefault.jpg?feature=og')
    	self.assertEqual(data['type'],'video')
    	self.assertEqual(data['url'], 'http://www.youtube.com/watch?v=q3ixBmDzylQ')
        
    def test_not_valid_url(self):
    	URL = "http://indf.tistory.com/"	
    	data = ExtendedOpenGraph.parse(url=URL)

    	print data 

    	self.assertEqual(data['title'],'INDF :: ')
    	self.assertEqual(data['image'] ,'http://i1.daumcdn.net/cfs.tistory/v/0/static/admin/editor/ccl_black04.png')
    	self.assertEqual(data['type'], 'website')
    	self.assertEqual(data['url'], 'http://indf.tistory.com/')
         
    
if __name__ == '__main__':
	unittest.main()