def area(length, width):
    a = length * width
    print(f'The area of a field {length}x{width} is of: {a}m².')
    return a

print(' Field Area Control')
print('-' * 20)

length = float(input('Length (m): '))
width = float(input('Width (m): '))
area(length, width)
