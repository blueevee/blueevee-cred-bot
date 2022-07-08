from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset
from rasa_sdk.types import DomainDict
from actions.enum.Enum import Message
import actions.Helpers as Helpers
from datetime import datetime as dtime
import pytz



class ActionRPG(Action):
    def name(self) -> Text:
        return "action_rpg_day"

    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        weekday = dtime.today().weekday()
        day_order = [4,3,2,1,0,6,5]

        return [
            SlotSet('days_remaining', day_order[weekday]),
            SlotSet('today_hour', dtime.today().hour),
            SlotSet('today_minute', dtime.today().minute),
            SlotSet('today_second', dtime.today().second)
            ]
class ActionMessageRPG(Action):
    def name(self) -> Text:
        return "action_choose_message_rpg"

    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        RPG_HOUR = 20
        days_remaining = tracker.get_slot('days_remaining')

        if days_remaining == 1:
            return dispatcher.utter_message(template="utter_2")
        elif days_remaining == 0:
            if dtime.today().hour < RPG_HOUR:
                return dispatcher.utter_message(template="utter_4")
            else:
                return dispatcher.utter_message(template="utter_5")

        elif days_remaining < 5:
            return dispatcher.utter_message(template="utter_1")
        else:
            return dispatcher.utter_message(template="utter_3")

class ActionWelcome(Action):
    def name(self) -> Text:
        return "action_welcome"

    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tz = pytz.timezone('America/Bahia')
        date = dtime.now(tz=tz)
        msg = None
        if date.hour >= 18:
            msg = Message.GOOD_EVENING.value
        elif date.hour >= 12:
            msg = Message.GOOD_AFTERNOON.value
        else:
            msg = Message.GOOD_MORNING.value

        return dispatcher.utter_message(f"{msg}! Esse é o canal de atendimento da `Blueevee Cred`, estou a disposição para te atender.\n\n💸 Posso te ajudar com algumas dúvidas sobre a nossa plataforma de empréstimos. Me pergunte algo!")

class ActionConfidenceFallback(Action):

    def name(self) -> Text:
        return "action_confidence_fallback"

    def run(self, dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_default")
        return []

class ValidateSimulatePersonalLoanForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simulate_personal_loan_form"

    def validate_personal_loan(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate personal loan value."""

        if Helpers.validate_personal_loan(slot_value):
            return {"personal_loan": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_loan")
            return {"personal_loan": None}

    def validate_personal_loan_term(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate personal loan term value."""

        if Helpers.validate_personal_loan_term(slot_value):
            return {"personal_loan_term": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_loan")
            return {"personal_loan_term": None}

class ValidateSimulatePropertyLoanForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simulate_property_loan_form"

    def validate_property_loan(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate property loan value."""

        if Helpers.validate_property_loan(slot_value):
            return {"property_loan": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_loan")
            return {"property_loan": None}

    def validate_property_loan_term(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate property loan term value."""

        if Helpers.validate_property_loan_term(slot_value):
            return {"property_loan_term": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_loan")
            return {"property_loan_term": None}

class ValidateSimulateCarLoanForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simulate_car_loan_form"

    def validate_car_loan(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate car loan value."""

        if Helpers.validate_car_loan(slot_value):
            return {"car_loan": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_loan")
            return {"car_loan": None}

    def validate_car_loan_term(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate car loan term value."""

        if Helpers.validate_car_loan_term(slot_value):
            return {"car_loan_term": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_loan")
            return {"car_loan_term": None}

class ValidateSimulateLoanForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simulate_loan_form"

    def validate_phone_number(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate phone number value."""

        if Helpers.validate_phone(slot_value):
            return {"phone_number": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_phone")
            return {"phone_number": None}

    def validate_email(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if Helpers.validate_email(slot_value):
            return {"email": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_email")
            return {"email": None}

    def validate_cpf(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate cpf value."""

        if Helpers.validate_cpf(slot_value):
            return {"cpf": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_cpf")
            return {"cpf": None}

    def validate_birth_date(self, slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate birth date value."""

        if Helpers.validate_older_than_18(slot_value):
            return {"birth_date": slot_value}
        else:
            dispatcher.utter_message(template="utter_wrong_birth_date")
            return {"birth_date": None}

    # def validate_marital_status(self, slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker, domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate marital_status value."""

    #     if Helpers.validate_marital_status(slot_value):
    #         return {"marital_status": slot_value}
    #     else:
    #         dispatcher.utter_message(template="utter_wrong_marital_status")
    #         return {"marital_status": None}
    # occupation:
    #   - type: from_text
       
class ActionCleanPersonalLoan(Action):

    def name(self):
        return "action_clean_personal_loan"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('personal_loan', None)]
       
class ActionCleanPersonalLoanTerm(Action):

    def name(self):
        return "action_clean_personal_loan_term"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('personal_loan_term', None)]
       
class ActionCleanPropertyLoan(Action):

    def name(self):
        return "action_clean_property_loan"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('property_loan', None)]
       
class ActionCleanPropertyLoanTerm(Action):

    def name(self):
        return "action_clean_property_loan_term"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('property_loan_term', None)]
       
class ActionCleanCarLoan(Action):

    def name(self):
        return "action_clean_car_loan"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('car_loan', None)]
       
class ActionCleanCarLoanTerm(Action):

    def name(self):
        return "action_clean_car_loan_term"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('car_loan_term', None)]
       
class ActionCleanName(Action):

    def name(self):
        return "action_clean_name"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('name', None)]
       
class ActionCleanCpf(Action):

    def name(self):
        return "action_clean_cpf"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('cpf', None)]
       
class ActionCleanMaritalStatus(Action):

    def name(self):
        return "action_clean_marital_status"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('marital_status', None)]
       
class ActionCleanBirthDate(Action):

    def name(self):
        return "action_clean_birth_date"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('birth_date', None)]
       
class ActionCleanOccupationData(Action):

    def name(self):
        return "action_clean_occupation_data"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('occupation', None)]
       
class ActionCleanPhoneNumber(Action):

    def name(self):
        return "action_clean_phone_number"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('phone_number', None)]
       
class ActionCleanEmail(Action):

    def name(self):
        return "action_clean_email"

    def run(self, dispatcher: CollectingDispatcher, 
    tracker: Tracker, 
    domain: Dict[Text, Any]) -> List[Dict]:

        return [SlotSet('email', None)]
