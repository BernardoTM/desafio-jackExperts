import re


def cpf_validate(cpf: str):

    cpf = re.sub('[^0-9]', '', cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False

    total_digit_one = 0
    for i, mult in enumerate(range(10, 1, -1)):
        total_digit_one += int(cpf[i]) * mult
    digit_one = total_digit_one % 11
    if digit_one < 2:
        if int(cpf[9]) != 0:
            return False
    else:
        if (11 - digit_one) != int(cpf[9]):
            return False

    total_digit_two = 0
    for i, mult in enumerate(range(11, 1, -1)):
        total_digit_two += int(cpf[i]) * mult
    digit_two = total_digit_two % 11
    if digit_two < 2:
        if int(cpf[10]) != 0:
            return False
    else:
        if (11 - digit_two) != int(cpf[10]):
            return False

    return True
