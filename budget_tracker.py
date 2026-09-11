def calculate_remaining(income, expenses):
  return income - expenses

income = float(input("2000: $"))

rent = float(input("417: $"))
transportation = float(input("200: $"))
food = float(input("200: $"))
entertainment = float(input("200: $"))

expenses = rent + transportation + food + entertainment

remaining = calculate_remaining(income, expenses):
print("money remaining:", remaining)
