# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
class ActionBuscar(Action):
    def name(self) -> Text:
        print('action_buscar')
        return "action_buscar"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        salida = []
        for i in ["elemento", "organismo", "nif", "numero"]:
            salida.extend([j for j in tracker.get_latest_entity_values(i)])

        dispatcher.utter_message(str(salida))
        return []
