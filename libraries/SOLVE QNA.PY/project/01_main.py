# Expense Tracker Project

expense = []

while True:

    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        category = input("Enter category: ")
        amount = int(input("Enter amount: "))

        expense.append({"category": category, "amount": amount})
        print("Expense added successfully ")

    elif choice == 2:
        if len(expense) == 0:
            print("No expenses added.")
        else:
            print("\n--- All Expenses ---")
            count = 1
            for item in expense:
                print(f"{count}. {item['category']} - {item['amount']}")
                count += 1

    elif choice == 3:
        total = 0
        for item in expense:
            total += item["amount"]

        print("\nTotal amount =", total)

    elif choice == 4:
        print("Thank you ")
        break

    else:
        print("Invalid choice . Try again.")