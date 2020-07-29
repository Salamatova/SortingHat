# coding=utf-8

from random import choice

students = []
file = open('students.txt', 'r') #'r' - read файл
students = file.read().splitlines() #прочитаем файл и сохраним его в массиве students,
# splitlines() - указывает на то, что каждая строка в файле является отдельным элементом массива.
print('Students:', students)
print()

faculties = []
file = open('faculties.txt', 'r')
faculties = file.read().splitlines()

teamA = []
teamB = []
teamC = []
teamD = []


NameA = choice(faculties)
faculties.remove(NameA)
NameB = choice(faculties)
faculties.remove(NameB)
NameC = choice(faculties)
faculties.remove(NameC)
NameD = choice(faculties)
faculties.remove(NameD)

while len(students)>0:
    studentA = choice(students)
    teamA.append(studentA)
    students.remove(studentA)

    if students == []:
        break

    studentB = choice(students)
    teamB.append(studentB)
    students.remove(studentB)

    if students == []:
        break

    studentC = choice(students)
    teamC.append(studentC)
    students.remove(studentC)

    if students == []:
        break

    studentD = choice(students)
    teamD.append(studentD)
    students.remove(studentD)

print(NameA, teamA)
print(NameB, teamB)
print(NameC, teamC)
print(NameD, teamD)