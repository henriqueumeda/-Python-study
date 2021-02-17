students = list()
individual = list()

while True:
    individual.append(input('Name: '))
    individual.append(float(input('First grade: ')))
    individual.append(float(input('Second grade: ')))
    students.append(individual[:])
    individual.clear()
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input('Do you want to continue [Y/N]? ').strip().upper()[0]
    if answer == 'N':
        break
print('-='*15)
print('{:<5}'.format('No.'), end='')
print('{:<20}'.format('NAME'), end='')
print('AVERAGE')
print('-'*30)
for counter, value in enumerate(students):
    print('{:<5}'.format(counter), end='')
    print('{:<20}'.format(value[0]), end='')
    average = (value[1] + value[2])/2
    print('{:.2f}'.format(average))

while True:
    show_grades = -1
    print('-'*30)
    while (show_grades < 0 or show_grades >= len(students)) and show_grades != 999:
        show_grades = int(input('Show grades of which student? (999 to stop the program): '))
    if show_grades == 999:
        break
    print(f'Grades of {students[show_grades][0]}: [{students[show_grades][1]}, {students[show_grades][2]}]')
