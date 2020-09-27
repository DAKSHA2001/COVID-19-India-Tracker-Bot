# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_search"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
          api_address = 'https://www.mohfw.gov.in/data/datanew.json'
          data_json = requests.get(api_address).json()
          
          entity_tracker = tracker.latest_message['entities']
          
          for i in entity_tracker:
              if i['entity'] == 'location':
                  name = i['value']
          
          message = "Please give me a valid state name in India"
          
          for i in range(0,35):
              if name.title() == data_json[i]['state_name']:
                  message = "Active_cases: {}".format(data_json[i]['active'])+"\nPositive_Count: {}".format(data_json[i]['positive'])+"\nCured_Count: {}".format(data_json[i]['cured'])+"\nDeath_Count: {}".format(data_json[i]['death'])+"\nNew_Active_Count: {}".format(data_json[i]['new_active'])+"\nNew_Positive_Count: {}".format(data_json[i]['new_positive'])+"\nNew_Cured_Count: {}".format(data_json[i]['new_cured'])+"\nNew_Death_Count: {}".format(data_json[i]['new_death'])+"\nState_Code: {}".format(data_json[i]['state_code'])
             
          dispatcher.utter_message(message)

          return []
