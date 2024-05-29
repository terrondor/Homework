my_dict = {'Dmitriy': 1990, 'Alex': 1995, 'Sveta': 2001}
print('Dict: ' + str(my_dict))

print('Existing vaalue: ' + str(my_dict['Dmitriy']))

print('Not existing value: ' + str(my_dict.get('Ola')))

my_dict.update({'Lera': 1989, 'Viktor': 1999})

suspended = my_dict.pop('Alex')

print('Delete value: ' + str(suspended))

print('Modified dictionary: ' + str(my_dict))



my_set = {1, 3, 3, True, False, True, 'Urban', 'Dmitriy', 'Urban'}

print(set(my_set))

my_set2 = {'World', 26,}

my_set |= my_set2                # Нашел метод со стороннего источника это краткая форма метода .update()
                                 # можно написать так my_set.udate(my_set2)
                                 # Не знаю на сколько это правильно

print(my_set)

my_set.remove('Dmitriy')
print(my_set)
















