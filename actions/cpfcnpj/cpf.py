from . import calculation as calc
from . import compatible as compat


def validate(cpf_number):

    _cpf = compat.clear_punctuation(cpf_number)

    if (len(_cpf) != 11 or
       len(set(_cpf)) == 1):
        return False

    first_part = _cpf[:9]
    second_part = _cpf[:10]
    first_digit = _cpf[9]
    second_digit = _cpf[10]

    if (first_digit == calc.calculate_first_digit(first_part) and
       second_digit == calc.calculate_second_digit(second_part)):
        return True

    return False
