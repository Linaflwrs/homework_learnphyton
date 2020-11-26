user = input("Сколько вам лет? ")
def age(user):
    if user <= 6:
        return 'Детский сад'
    elif  7 <= user <= 17:
        return 'Школа'
    elif 18 <= user <= 23:
        return 'Вуз'
    elif 24 <= user <= 65:
        return 'Работа'
    else:
        return 'Другое'
print(age(int(user)))