grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

avanger_grades0 = sum(grades[0]) / len(grades[0])
print(avanger_grades0)
avanger_grades1 = sum(grades[1]) / len(grades[1])
print(avanger_grades1)
avanger_grades2 = sum(grades[2]) / len(grades[2])
print(avanger_grades2)
avanger_grades3 = sum(grades[3]) / len(grades[3])
print(avanger_grades3)
avanger_grades4 = sum(grades[4]) / len(grades[4])   # Пытался найти и разобраться как написать функцию или цикл чтобы
print(avanger_grades4)                              #свести все это по максимому в минимум строк но не хватает еще пока знаний

grades[0] = 4.0
grades[1] = 2.25
grades[2] = 4.0
grades[3] = 3.6666666666666665
grades[4] = 4.8
print(grades)

students = sorted(students)
print(students)
students_lst = list(students)
print(students_lst)

dct_ = dict(zip(students_lst, grades))
print(dct_)

# Также можно применив циклы и функции написать так чтобы преподоватьель вводил оценки через input() и -
# -  pyton все обсчитате , пока не хватает понимания работы циклов и функций