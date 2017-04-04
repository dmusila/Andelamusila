''' Assumation made : Time can be more than a year'''

def loan_calculator(amount, rate, time):
    total_amount = (amount * rate/100 * time/12) + amount
    return total_amount

print(loan_calculator(3000,30,30))