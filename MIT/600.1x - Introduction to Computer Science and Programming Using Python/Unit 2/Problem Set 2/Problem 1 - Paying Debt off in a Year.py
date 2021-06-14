balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12

for month in range(1, 13):
    minimum_monthly_payment = monthlyPaymentRate*balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    balance = monthly_unpaid_balance + (monthlyInterestRate * monthly_unpaid_balance)

print('Remaining balance: {:.2f}'.format(balance))
