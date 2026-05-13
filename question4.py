# Expense Splitter Among Friends

expenses = [1200, 850, 1500, 950]

# Total expense
total_expense = sum(expenses)

# Average share
average_share = total_expense / len(expenses)

# Person who paid highest
highest_paid = max(expenses)
person = expenses.index(highest_paid) + 1

print("Total Expense:", total_expense)
print("Average Share:", average_share)
print("Person", person, "paid the highest amount:", highest_paid)

# Amount each friend should contribute equally
for i in range(len(expenses)):
    difference = expenses[i] - average_share

    if difference > 0:
        print("Person", i + 1, "should receive", difference)
    else:
        print("Person", i + 1, "should pay", abs(difference))