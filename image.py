#!/usr/bin/env python
import urllib2
from urlparse import urlsplit
from BeautifulSoup import BeautifulSoup # for HTML parsing
from urllib2 import urlopen
import urllib
import os.path
# use this image scraper from the location that 
#you want to save scraped images to
class imageDownloader(object):
    
    image_ext_list = ['.jpeg', '.png', '.tif', '.tiff', '.gif', '.jpg', '.jif', '.jfif']
    
    def __init__(self):
        pass
    
    def make_soup(self, url):
        html = urlopen(url).read()
        return BeautifulSoup(html)
    
    def get_images(self, url):
        soup = self.make_soup(url)
        
        images = [img for img in soup.findAll('img')]
        print (str(len(images)) + "image type enbtity found found.")
        print 'Downloading them to current working directory if the image file type in known to us.'
        #compile our unicode list of image links
        image_links = [each.get('src') for each in images]
        
        for each in image_links:
            
            filename=each.split('/')[-1]
            extension = os.path.splitext(filename)[1]
            
            if extension in imageDownloader.image_ext_list:                 #checking whether it is actually and image or not
                if not each.startswith('http:'):        #ensuring that http is present in the url of image
                    each = 'http:' + each
    
                urllib.urlretrieve(each, filename)
        return image_links
