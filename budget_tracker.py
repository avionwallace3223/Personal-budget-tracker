def calculate_remaining(income, expenses):
  return income - expenses

income = float(input("Enter your monthly income: $"))

rent = float(input("How much do you spend on rent?: $"))
transportation = float(input("How much do you spend of transportation?: $"))
food = float(input("How much do you spend on food?: $"))
entertainment = float(input("How much do you spend on entertainment: $"))

expenses = rent + transportation + food + entertainment

remaining = calculate_remaining(income, expenses)
print("money remaining:", remaining)
