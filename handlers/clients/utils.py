from re import findall


def only_cyrillic(string):
    cyrillic_count = findall(string=string, pattern="[а-яА-Я]")
    return len(cyrillic_count) == len(string)


def correct_amount(amount, client_account):
    digit_count = findall(string=amount, pattern="[0-9]")
    if len(digit_count) != len(amount):
        return False
    if int(amount) > client_account:
        return False
    return True


def correct_update_amount(amount):
    digit_count = findall(string=amount, pattern="[0-9]")
    return len(digit_count) == len(amount)


def correct_full_name(full_name):
    try:
        last_name, first_name, middle_name = full_name.split(' ')
        if only_cyrillic(last_name) and only_cyrillic(first_name) and only_cyrillic(middle_name):
            return True
        else:
            return False
    except ValueError:
        return False


def correct_card_number(card_number):
    card_number = card_number.replace(' ', '')
    try:
        int(card_number)
        return len(card_number) == 16
    except ValueError:
        return False


def split_card_number(card_number):
    card_number = card_number.replace(' ', '')
    return f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}'


