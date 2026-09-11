def calculate_remaining(income, expenses):
  return income - expenses

income = float(input("Enter your monthly income: $"))

rent = float(input("How much do you spend on rent?: $"))
transportation = float(input("How much do you spend of transportation?: $"))
food = float(input("How much do you spend on food?: $"))
entertainment = float(input("How much do you spend on entertainment: $"))

expenses = rent + transportation + food + entertainment

remaining = calculate_remaining(income, expenses)
print("\n===== MONTHLY BUDGET =====")
print(f"Income: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Transportation: ${transportation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Entertainment: ${entertainment:.2f}")

print(f"Total Expenses: ${expenses:.2f}")
print(f"Money Remaining: ${remaining:.2f}")
print("==========================")

if remaining < 0:
    print("Warning: You are over budget!")
else:
    print("You are within your budget!")
    
