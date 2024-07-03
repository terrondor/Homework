class House:
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floor or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.numbers_of_floor

    def __str__(self):
        return f'Название:{self.name}, кол-во этажей: {self.numbers_of_floor}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)

print(len(h1))
print(len(h2))
