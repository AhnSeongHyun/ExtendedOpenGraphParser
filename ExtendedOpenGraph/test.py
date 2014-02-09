# -*- coding: utf-8 -*-


# encoding: utf-8

import unittest
import ExtendedOpenGraph


valid_html = """
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


non_valid_html = """
<html>
<head>
<title>The Rock (1996)</title>
</head>
<body>
<img src = "./gif"/>
<img src = "http://pdnf.png"/>
</html>
"""


class Test(unittest.TestCase):

    def test_valid_html(self):
        data = ExtendedOpenGraph.parse(html=valid_html)
        self.assertEqual(data['title'], 'The Rock')
        self.assertEqual(data['image'], 'http://ia.media-imdb.com/images/rock.jpg')
        self.assertEqual(data['type'], 'movie')
        self.assertEqual(data['url'], 'http://www.imdb.com/title/tt0117500/')
    
    def test_not_valid_html(self):
        data = ExtendedOpenGraph.parse(html=non_valid_html)
        
        self.assertEqual(data['title'], 'The Rock (1996)')
        self.assertEqual(data['image'], 'http://pdnf.png')
        self.assertEqual(data['type'], 'website')
        self.assertEqual(data['url'], None)

    def test_valid_url(self):
        url = "http://www.youtube.com/watch?v=q3ixBmDzylQ"
        data = ExtendedOpenGraph.parse(url=url)

        self.assertEqual(data['title'], 'While My Guitar Gently Weeps')
        self.assertEqual(data['type'], 'video')
        self.assertEqual(data['url'], 'http://www.youtube.com/watch?v=q3ixBmDzylQ')

        #print data
        
    def test_not_valid_url(self):
        url = "http://indf.tistory.com/"
        data = ExtendedOpenGraph.parse(url=url)

        self.assertEqual(data['title'], 'INDF :: ')
        self.assertEqual(data['image'], '/favicon.ico')
        self.assertEqual(data['type'], 'website')
        self.assertEqual(data['url'], 'http://indf.tistory.com')

    def test_urls(self):
        urls = [
                "http://www.twitter.com",
                "http://github.com",
                "http://facebook.com",
                "http://amazon.com",
                "http://naleejang.tistory.com",
                "http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html#contents"
                ]
        try:

            for url in urls:    
                ExtendedOpenGraph.parse(url=url)
        except Exception, e:
            raise
        else:
            pass
        finally:
            pass


if __name__ == '__main__':
    unittest.main()









