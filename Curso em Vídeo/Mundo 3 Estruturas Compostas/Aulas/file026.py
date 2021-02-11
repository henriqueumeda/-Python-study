guys = list()
data = list()
adults = junior = 0
for counter in range(0, 3):
    data.append(str(input('Name: ')))
    data.append(int(input('Age: ')))
    guys.append(data[:])
    data.clear()

print(guys)

for person in guys:
    if person[1] >= 21:
        print(f'{person[0]} has reached the legal age of majority.')
        adults += 1
    else:
        print(f"{person[0]} hasn't reached the legal age of majority.")
        junior += 1

print(f'Number of adults: {adults}')
print(f'Number of juniors: {junior}')
