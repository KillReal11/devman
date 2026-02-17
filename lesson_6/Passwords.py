def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(i.isdigit() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isdigit() and not i.isalpha() for i in password)


def main():
    password = input("Введите пароль: ")
    score = 0
    verification = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    for v in verification:
        if v(password):
            score += 2
    print("Рейтинг пароля: ", score)


if __name__ == '__main__':
    main()
