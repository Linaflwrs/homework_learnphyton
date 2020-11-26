def wether(temperature):
    if temperature <= 0:
        return 'cold'
    elif 1 <= temperature <= 15:
        return 'warm'
    elif 16 <= temperature <= 25:
        return 'very warm'
    else: 
        return 'another' 

print(wether(10))
print(wether(-10))
print(wether(30))



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

