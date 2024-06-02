first = int(input('Введите число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print('3')
elif first == second or first == third or second == first or second == third:
    print('2')
else:
    print('0')