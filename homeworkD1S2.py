def stroki(one, two):
    one = str(one)
    two = str(two)
    if one.isdigit() + two.isdigit():
        return 0
    if one == two:
        return 1
    if len(one) > len(two):
        return 2
    elif two == 'learn':
        return 3  
    

print(stroki(1, 2))
print(stroki('one', 'one'))
print(stroki('oneee', 'one'))
print(stroki('oneee', 'learn'))