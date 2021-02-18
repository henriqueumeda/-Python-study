balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12
initial_balance = balance
monthly_lower_bound = balance/12
monthly_higher_bound = (balance * (1 + monthlyInterestRate)**12)/12
payment = (monthly_higher_bound + monthly_lower_bound)/2
epsilon = 0.01

while abs(balance) >= epsilon and abs(monthly_higher_bound - monthly_lower_bound) > epsilon:
    for month in range(1, 13):
        monthly_unpaid_balance = balance - payment
        balance = monthly_unpaid_balance + (monthlyInterestRate * monthly_unpaid_balance)
    if balance > 0:
        monthly_lower_bound = payment
    else:
        monthly_higher_bound = payment
    payment = (monthly_higher_bound + monthly_lower_bound) / 2
    balance = initial_balance

print('Lowest Payment: {:.2f}'.format(payment))
