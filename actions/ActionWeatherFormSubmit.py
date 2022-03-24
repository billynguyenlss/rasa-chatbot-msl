from datetime import date, timedelta
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionWeatherFormSubmit(Action):
    def name(self) -> Text:
        return "action_weather_form_submit"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("address")
        text_date = tracker.get_slot("date")
        # query_date = self._get_date(text_date)

        msg = f"Thời tiết hôm nay tại {city} là {text_date}"
        dispatcher.utter_message(msg)

        return []

    def _get_date(self, text_date):
        if text_date in ["hôm nay", "hom nay"]:
            return date.today()
        if text_date in ["ngày mai", "ngay mai", "tomorrow"]:
            tomorrow = date.today() + timedelta(days=1)
            return tomorrow
        if text_date in ["hôm qua", "hom qua", "yesterday"]:
            yesterday = date.today() - timedelta(days=1)
            return yesterday
        return date.today()
