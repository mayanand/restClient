#!/usr/bin/env python
from restapi import restAPI
import urllib
import pprint
import time

class googleRestAPI(restAPI):
    
    def __init__(self):
        restAPI.__init__(self)
        
        self.RESTendpoint = "https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q=%s"
        
        
    def parseGoogleJSON(self, topic):
        
        result = self.connect_api(topic)
            
        for element in result['responseData']['results']:
            print element['image']['url']
            res = urllib.urlretrieve((element['image']['url']), str(time.time()).replace('.','_'))
            print res
        #pprint.pprint(result)

if __name__ == '__main__':
    
    g_obj = googleRestAPI()
    g_obj.parseGoogleJSON('obama')
