import re
from datetime import datetime
from actions.cpfcnpj import cnpj, cpf


def validate_cpf(cpf_number: str):
    return cpf.validate(cpf_number)

def validate_cnpj(cnpj_number: str):
    return cnpj.validate(cnpj_number)

def validate_email(email: str):
    email = email.strip()
    if re.match(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email):
        return True
    return False

def validate_phone(telephone: str):
    telephone = telephone.strip()
    if re.match(r'^\(?( ?\d{2}|0\d{2}) ?\)? ?(\d{5}|\d{4})[ .-]?(\d{4})$', telephone):
        return True
    return False

def validate_personal_loan(value: str):
    try:
        return float(value) <= 35000 and float(value) >= 1000
    except:
        return False

def validate_personal_loan_term(value: str):
    try:
        return float(value) <= 24 and float(value) >= 2
    except:
        return False

def validate_property_loan(value: str):
    try:
        return float(value) <= 3000000 and float(value) >= 10000
    except:
        return False

def validate_property_loan_term(value: str):
    try:
        return float(value) <= 240 and float(value) >= 2
    except:
        return False

def validate_car_loan(value: str):
    try:
        return float(value) <= 300000 and float(value) >= 40000
    except:
        return False

def validate_car_loan_term(value: str):
    try:
        return float(value) <= 60 and float(value) >= 2
    except:
        return False

def validate_older_than_18(date: str):
    try:
        user_date = datetime.strptime(date, "%d/%m/%Y")
        current_year = datetime.now().year
        limit_date = datetime.now()
        limit_date = limit_date.replace(year=current_year-18)
        return user_date <= limit_date
    except:
        return False