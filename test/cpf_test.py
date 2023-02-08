import src.util.cpf as cpf


def test_cpf_invalid_less_11_digit():
    assert cpf.cpf_validate("047226613") == False


def test_cpf_invalid_bigger_11_digit():
    assert cpf.cpf_validate("04722661113") == False


def test_cpf_invalid_repitede_digit():
    assert cpf.cpf_validate("11111111111") == False


def test_cpf_first_digit_invalid():
    assert cpf.cpf_validate("80495339160") == False


def test_cpf_first_second_invalid():
    assert cpf.cpf_validate("52757924098") == False


def test_cpf_valid():
    assert cpf.cpf_validate("165.570.151-76") == True
