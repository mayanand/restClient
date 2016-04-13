#!/usr/bin/env python

import urllib2
import simplejson
import pprint

class restAPI(object):
    
    def __init__(self):
        
        self.RESTendpoint = ''
        self.apiKey = ''
        self.referrer = ''

    def connect_api(self, topic):
        
        if self.apiKey:
            self.RESTendpoint = self.RESTendpoint %(topic, self.apiKey)
            
        else:
            self.RESTendpoint = self.RESTendpoint %(topic)

        request = urllib2.Request(self.RESTendpoint, None, {'Referer': self.referrer})
        response = urllib2.urlopen(request)
        
        ## Process the JSON string.
        results = simplejson.load(response)
        
        #pprint.pprint(results)
        return results        