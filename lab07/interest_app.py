import locale
from interest import investment_value


print("Welcome to the interest app!")


print(locale.currency(investment_value(start=1000, interest_rate=0.05,
      tax_rate=0, deposit=0, years=10)))
