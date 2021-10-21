from re import findall


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


