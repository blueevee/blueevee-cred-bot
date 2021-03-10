from enum import Enum

class Message(Enum):
    ERROR_TYPE = "variable type error. waiting {}"
    GOOD_MORNING = "Bom dia"
    GOOD_AFTERNOON = "Boa Tarde"
    GOOD_EVENING = "Boa Noite"
