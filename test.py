# -*- coding: utf-8 -*-


# encoding: utf-8

import unittest
import ExtendedOpenGraph



VALID_HTML = """
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



NOT_VALID_HTML = """
<html>
<head>
<title>The Rock (1996)</title>
</head>
<body>
<img src = "./gif"/>
<img src = "http://pdnf.png"/>
</html>
"""



class test(unittest.TestCase):

    def test_valid_html(self):
    	data = ExtendedOpenGraph.parse(html=VALID_HTML)
        self.assertEqual(data['title'],'The Rock')
        self.assertEqual(data['image'] ,'http://ia.media-imdb.com/images/rock.jpg')
        self.assertEqual(data['type'],'movie')
        self.assertEqual(data['url'], "http://www.imdb.com/title/tt0117500/")
        #print data
    
    def test_not_valid_html(self):
        data = ExtendedOpenGraph.parse(html=NOT_VALID_HTML)
        self.assertEqual(data['title'],'The Rock (1996)')
        self.assertEqual(data['image'] ,'http://pdnf.png')
        self.assertEqual(data['type'],'website')
        self.assertEqual(data['url'], None)
        #print data

    def test_valid_url(self):
    	URL = "http://www.youtube.com/watch?v=q3ixBmDzylQ"
    	data = ExtendedOpenGraph.parse(url=URL)

    	self.assertEqual(data['title'],'While My Guitar Gently Weeps')
    	self.assertEqual(data['image'] ,'http://i1.ytimg.com/vi/q3ixBmDzylQ/hqdefault.jpg?feature=og')
    	self.assertEqual(data['type'],'video')
    	self.assertEqual(data['url'], 'http://www.youtube.com/watch?v=q3ixBmDzylQ')

        #print data
        
    def test_not_valid_url(self):
    	URL = "http://indf.tistory.com/"	
    	data = ExtendedOpenGraph.parse(url=URL)
 
    	self.assertEqual(data['title'],'INDF :: ')
    	self.assertEqual(data['image'] ,'http://i1.daumcdn.net/cfs.tistory/v/0/static/admin/editor/ccl_black04.png')
    	self.assertEqual(data['type'], 'website')
    	self.assertEqual(data['url'], 'http://indf.tistory.com/')
        
        #print data
    
if __name__ == '__main__':
	unittest.main()