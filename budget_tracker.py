def calculate_remaining(income, expenses):
  return income - expenses

income = float(input("Enter your monthly income: $"))

expenses = []
amounts = []

while True:
   category = input("Enter an expense category: ")

   if category.lower() == "done":
       break 

   amount = float(input("Enter the amount: $"))

   expenses.append(category)
   amounts.append(amount)

custom_expenses = sum(amounts)

rent = float(input("How much do you spend on rent?: $"))
transportation = float(input("How much do you spend of transportation?: $"))
food = float(input("How much do you spend on food?: $"))
entertainment = float(input("How much do you spend on entertainment: $"))

total_expenses = rent + transportation + food + entertainment + custom_expenses

remaining = calculate_remaining(income, total_expenses)
savings_percentage = (remaining / income) * 100

print("\n===== MONTHLY BUDGET =====")
print(f"Income: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Transportation: ${transportation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Entertainment: ${entertainment:.2f}")

print("\nCustome Expenses:")

for i in range(len(expenses)):
  print(f"{expenses[i]}: ${amounts[i]:.2f}" )

print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Money Remaining: ${remaining:.2f}")
print(f"Savings Percentage: {savings_percentage:.1f}%")
print("==========================")

if remaining < 0:
    print("Warning: You are over budget!")
else:
    print("You are within your budget!")
    
