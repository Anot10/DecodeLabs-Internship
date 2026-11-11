
total = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense == "done":
        break

    total = total + float(expense)

print("\nTotal Spent: Rs.", total)
