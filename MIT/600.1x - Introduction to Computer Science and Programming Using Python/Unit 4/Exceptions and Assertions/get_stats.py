def get_stats(class_list):
    new_stats = []
    for element in class_list:
        new_stats.append([element[0], element[1], average(element[1])])
    return new_stats

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
               [['deadpool'], []]]

def average(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0

print(get_stats(test_grades))
