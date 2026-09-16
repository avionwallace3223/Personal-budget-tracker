def calculate_remaining(income, expenses):
  return income - expenses

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            
            if amount < 0:
                print("Expenses cannot be negative.")
                continue
            return amount
        except ValueError:
            print("Please enter valid number.")
            
income = get_amount("Enter your monthly income: $")

expenses = []
amounts = []

while True:
    category = input("Enter an expense category: ")

    if category.lower() == "done":
        break 

    while True:
        try:
            amount = get_amount("Enter the amount: $")
            
            if amount < 0:
               print("Expense cannot be negative")
               continue 
              
            break
            
        except ValueError:
           print("Please enter a valid number.")
  
    expenses.append(category)
    amounts.append(amount)

custom_expenses = sum(amounts)

rent = get_amount("How much do you spend on rent?: $")
transportation = get_amount("How much do you spend of transportation?: $")
food = get_amount("How much do you spend on food?: $")
entertainment = get_amount("How much do you spend on entertainment: $")

total_expenses = rent + transportation + food + entertainment + custom_expenses

remaining = calculate_remaining(income, total_expenses)
savings_percentage = (remaining / income) * 100
  
all_expenses = list(zip(expenses, amounts))
largest_expense = max(all_expenses, key=lambda expense: expense[1])

print("\n===== MONTHLY BUDGET =====")
print(f"Income: ${income:.2f}")
print(f"Rent: ${rent:.2f}")
print(f"Transportation: ${transportation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Entertainment: ${entertainment:.2f}")
print("\nCustom Expenses:")
print(f"Largest Custom Expense: {largest_expense[0]} ${largest_expense[1]:.2f}")

for i in range(len(expenses)):
  print(f"{expenses[i]}: ${amounts[i]:.2f}" )

print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Money Remaining: ${remaining:.2f}")
print(f"Savings Percentage: {savings_percentage:.1f}%")
if remaining > 0:
    print(f"You saved ${remaining:.2f} this month!")
elif remaining == 0: 
      print(" You broke even this month.")
else:
    print(f"You overspent by ${abs(remaining):.2f} this month.")
    
print("==========================")

if remaining < 0:
    print("Warning: You are over budget!")
else:
    print("You are within your budget!")
    
