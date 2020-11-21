a = 2
b = 0.5
print (a + b)
name = 'l0na'.replace('0', 'i')
b = f'hello {name}!'.capitalize()
print(b)
a = 'lina love ice_creem'
print(a.split( ))
#v = int(input('Введите число от 1 до 10: '))
#print(v + 10) 
# поправьте код, чтобы выводилось число
# на 10 больше, чем введённое
# например, пользователь ввел 10 
# программа вывела 20
#name = (input('Введите ваше имя: '))
#b = f'Привет, {name}! Как дела'
print(b)
#print(???) # поправьте код, чтобы выводилась строка
 #			# Привет, ИМЯ! Как дела

 #Выведите на экран при помощи print() результат работы:

float('1')  # ???
#int('2.5')  # ???
bool(1)  # ???
bool('')  # ???
bool(0)  # ???
print()

nambers = [3, 5, 7, 9 , 10.5 ]
nambers.append('python')
print(len(nambers))
print(nambers[0])
print(nambers[-1])
print(nambers[1 : 4])
nambers.remove('python')
print(nambers)

#place_wether = {
 #   "city" : "Москва",
  #  "temperature" : '20',
#}
#print(place_wether['city'])
#place_wether[ "temperature"] = int(place_wether[ "temperature"]) - 5
#print(place_wether["temperature"])
#print(place_wether)
#(printplace_wether.get("country","Россия"))
#print(place_wether)
#place_wether["date"] = "27.05.2019"
#print(place_wether)

def get_summ(one, two, delimiter='&'):
    a = str(one)
    b = str(two)
    print(a +delimiter+ b)
one = 'lern'
two = 'python'
get_summ(one, two)
