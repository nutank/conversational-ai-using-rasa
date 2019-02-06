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
        # return <name_of_the_action> 

    def run(self, dispatcher, tracker, domain):
        
        # code to handle what the action will do