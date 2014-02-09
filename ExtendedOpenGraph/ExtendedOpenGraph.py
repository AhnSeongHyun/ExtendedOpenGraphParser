# -*- coding: utf-8 -*-
 
import opengraph
import urllib2

try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


def parse(url=None, html=None):

    if url is None and html is not None:
        return parse_html(html)

    elif url is not None:
        return parse_url(url)

    else:
        raise Exception("url and html are None.")


def parse_html(html):
    ogp_result = opengraph.OpenGraph(html=html)

    if ogp_result.is_valid() is True:
        return parse_valid_html(html, ogp_result)

    else:
        return parse_non_valid_html(html)


def parse_valid_html(html, ogp_result):
    parse_result = dict()

    for key in ogp_result.keys():
        parse_result[key] = ogp_result[key]

    # pop _url
    if ('_url' in parse_result) is True:
        parse_result.pop("_url", None)

    # if required factor, must get.
    if ('url' in parse_result) is False:
        parse_result['url'] = get_url(html=html)

    if ('image' in parse_result) is False:
        parse_result['image'] = get_image(html)

    if ('title' in parse_result) is False:
        parse_result['title'] = get_title(html)

    if ('type' in parse_result) is False:
        parse_result['type'] = get_type(html=html)

    return parse_result


def parse_non_valid_html(html):
    parse_result = dict()

    parse_result['title'] = get_title(html)
    parse_result['image'] = get_image(html)
    parse_result['url'] = get_url(html=html)
    parse_result['type'] = get_type(html=html)

    return parse_result


def parse_url(url):
    ogp_result = opengraph.OpenGraph(url=url)

    if ogp_result.is_valid():
        return parse_valid_url(url, ogp_result)
    else:
        return parse_non_valid_url(url)


def parse_valid_url(url, ogp_result):

    parse_result = {}

    for key in ogp_result.keys():
        parse_result[key] = ogp_result[key]

    # pop _url
    if ('_url' in parse_result) is True:
        parse_result.pop("_url", None)

    html = get_html(url)

    # if required factor, must get.
    if ('url' in parse_result) is False:
        parse_result['url'] = get_url(url=url)

    if ('image' in parse_result) is False:
        parse_result['image'] = get_image(html)

    if ('title' in parse_result) is False:
        parse_result['title'] = get_title(html)

    if ('type' in parse_result) is False:
        parse_result['type'] = get_type(url=url)

    return parse_result


def parse_non_valid_url(url):

    #getHtml from url
    parse_result = {}
    html = get_html(url)

    parse_result['title'] = get_title(html)
    parse_result['image'] = get_image(html)
    parse_result['url'] = get_url(url=url)
    parse_result['type'] = get_type(html=html)

    return parse_result


def get_image(html=None):

    if html:
        soup = BeautifulSoup(html)
        img_url = get_meta_itemprop_image(soup)

        if img_url:
            return img_url
        else:
            img_url = get_link_rel_shortcut_icon(soup)

            if img_url:
                return img_url
            else:
                return get_main_image(soup)

def get_link_rel_shortcut_icon(soup=None):
    if soup:

        link_tags = soup.html.head.find_all('link')

        img_url = None
        for link_tag in link_tags:
            link_tag_rel = link_tag.get('rel')
            if link_tag_rel is not None \
                and u'shortcut' in link_tag_rel \
                and u'icon' in link_tag_rel:

                img_url = link_tag.get('href')
                break



    return img_url

def get_meta_itemprop_image(soup=None):

    if soup:
        meta_tags = soup.html.head.find_all('meta')

        img_url = None
        for meta_tag in meta_tags:
            if meta_tag.get('itemprop') == 'image':
                img_url = meta_tag.get('content')
                break

    return img_url


def get_main_image(soup=None):
    main_image = ''
    if soup:
        images = soup.html.find_all('img')

        for image in images:
            if image.has_attr('src') is True:
                if '.gif' not in image['src']:
                    main_image = image['src']  # first image

    return main_image


def get_url(url=None, html=None):

    if url:
        last_idx = url.rfind("/")
        if url[last_idx-1] == "/":  # it is http://
            return url
        else:
            return url[:last_idx]
    else:
        return None


def get_type(url=None, html=None):
    # default 'website'
    return 'website'


def get_title(html):
    soup = BeautifulSoup(html)
    return soup.html.head.title.contents[0]


def get_html(url):
    raw = urllib2.urlopen(url)
    html = raw.read()
    return html


if __name__ == '__main__':
    print parse(url='http://facebook.com')
