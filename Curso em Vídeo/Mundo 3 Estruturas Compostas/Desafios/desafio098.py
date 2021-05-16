from time import sleep

def counting(initial_number, final_number, step):
    print('-=' * 20)
    if step == 0:
        step = 1
    print(f'Couting from {initial_number} to {final_number} by step {step}')

    if step > 0:
        final_number += 1
    else:
        final_number -= 1
    for i in range(initial_number, final_number, step):
        print(i, end=' ')
        sleep(0.5)
    print('END!')


# counting(1, 10, 1)
# counting(10, 0, -2)

print('-=' * 20)
print("Now it's your turn to custom the counting!")

while True:
    try:
        initial_number = int(input('Initial: '))
        final_number = int(input('Final: '))
        step = int(input('Step: '))
        counting(initial_number, final_number, step)
        break
    except ValueError:
        print('Entry is not an integer. Please try again.')
