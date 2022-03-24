# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime, date, timedelta

class ActionQueryTime(Action):

    def name(self) -> Text:
        return "action_query_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_time = datetime.now().strftime("It's %H:%M:%S")

        dispatcher.utter_message(text=current_time)

        return []

class ActionQueryDate(Action):

    def name(self) -> Text:
        return "action_query_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text_date = tracker.get_slot("date")

        int_date = text_date_to_int(text_date)
        dispatcher.utter_message(text=int_date)

        return []

def text_date_to_int(text_date):
    if text_date in ["hôm nay","hom nay"]:
        return date.today().strftime('%Y-%m-%d')
    if text_date in ["ngày mai", "ngay mai", "tomorrow"]:
        tomorrow = date.today() + timedelta(days=1)
        return tomorrow.strftime('%Y-%m-%d')
    if text_date in ["hôm qua","hom qua","yesterday"]:
        yesterday =  date.today() - timedelta(days=1)
        return yesterday.strftime('%Y-%m-%d')
    return []