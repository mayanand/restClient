#!/usr/bin/env python
from restapi import restAPI
from image import imageDownloader

class guardianRestAPI(restAPI):
    
    def __init__(self):
        restAPI.__init__(self)
        
        self.RESTendpoint = "http://content.guardianapis.com/search?q=%s&api-key=%s"
        self.apiKey = 'test'
        
        
    def parseGuradianJSON(self, topic):
        result = self.connect_api(topic)
        
        imageDownloader_obj = imageDownloader()
        for element in result['response']['results']:
            imageDownloader_obj.get_images(element['webUrl'])
        
        
        #pprint.pprint(result)

if __name__ == '__main__':
    
    g_obj = guardianRestAPI()
    g_obj.parseGuradianJSON('obama')
