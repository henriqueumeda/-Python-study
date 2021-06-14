balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
initial_balance = balance
payment = balance/12 // 10 * 10

while balance > 0:
    balance = initial_balance
    payment += 10
    for month in range(1, 13):
        monthly_unpaid_balance = balance - payment
        balance = monthly_unpaid_balance + (monthlyInterestRate * monthly_unpaid_balance)

print('Lowest Payment: {:.2f}'.format(payment))
