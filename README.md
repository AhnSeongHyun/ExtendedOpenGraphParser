ExtendedOpenGraphParser is a python module for parsing the Open Graph ProtocoL. 
Open Graph Protocol spec: http://ogp.me/


##Installation
pip install ExtendedOpenGraph

##Features
<li> Based on opengraph </li>
<li> If not exist Open Graph properties in meta tag, it is able to parse basic Metadata.</li>
<li> Input URL and HTML.</li>
<li> Output python dictionary </li>
<li> Like Facebook. </li>


##Usage 
<b>input : url </b>

    >>> import ExtendedOpenGraph
	>>> data = ExtendedOpenGraph.parse(url="http://www.twitter.com")
	>>> for key, value in data.items():
	...     print "%-15s => %s" % (key, value)
	...
	url             => http://www.twitter.com
	image           => https://abs.twimg.com/a/1373572090/t1/img/front_page/jp-mountain@2x.jpg
	type            => website
	title           => 트위터 

<b> input : html </b>

	>>> ex_html="<html><head><title>ExtendOpenGraph</title></head><body><img src='logo.png'/></body></html>"
	>>> data = ExtendedOpenGraph.parse(html=ex_html)
	>>> for key, value in data.items():
	...     print "%-15s => %s" % (key, value)
	...
	url             => None
	image           => logo.png
	type            => website
	title           => ExtendOpenGraph
    
    
    