def lifetime(user_age):

    if user_age <= 6:
        return 'Детский сад'
    elif  7 <= user_age <= 17:
        return 'Школа'
    elif 18 <= user_age <= 23:
        return 'Вуз'
    elif 24 <= user_age <= 66:
        return 'Работа'
    else:
        return 'Другое'
user_age = input("Сколько вам лет? ")
print(lifetime(int(user_age)))