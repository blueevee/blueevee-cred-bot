DIVISOR = 11

CPF_WEIGHTS = ((10, 9, 8, 7, 6, 5, 4, 3, 2),
              (11, 10, 9, 8, 7, 6, 5, 4, 3, 2))
CNPJ_WEIGHTS = ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
               (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2))



def calculate_first_digit(number):
    sum = 0
    if len(number) == 9:
        weights = CPF_WEIGHTS[0]
    else:
        weights = CNPJ_WEIGHTS[0]

    for i in range(len(number)):
        sum = sum + int(number[i]) * weights[i]
    rest_division = sum % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)


def calculate_second_digit(number):
    sum = 0
    if len(number) == 10:
        weights = CPF_WEIGHTS[1]
    else:
        weights = CNPJ_WEIGHTS[1]

    for i in range(len(number)):
        sum = sum + int(number[i]) * weights[i]
    rest_division = sum % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)
