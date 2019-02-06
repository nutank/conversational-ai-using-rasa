# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)


class ApiAction(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_retrieve_image" 

    def run(self, dispatcher, tracker, domain):
        
        group = tracker.get_slot('group')

        print ("Group " + group)
        
        r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(group))
        response = r.content.decode()

        print ("Response content " + response)


        response = response.replace('["',"")
        response = response.replace('"]',"")

        print ("Unformatted response" + response)
   
        
        #display(Image(response[0], height=550, width=520))
        dispatcher.utter_message("Here is something to cheer you up: {}".format(response))