import json
expenses = []
n= int(input("how many expences added:"))
for i in range(n):
    name = input("work of expences:")
    amount = float(input("Amount :"))
    expense = {"name" : name,"amount" : amount}
    expenses.append(expense)
total  = sum(expense["amount"] for expense in expenses)
print("Total Expense :", total)
with open("expenses.json", "w") as f:
    json.dump(expenses, f ,indent=4)
print("saved to expense.json!")
