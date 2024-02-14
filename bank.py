# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List last 10 transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        deposit_add = int(input("How much do you want to deposit?\n"))
        transactions.append(deposit_add)
        pass
    elif choice == '2':
        withdraw_remove = int(input("How much do you want to withdraw?\n"))
        transactions.append(-withdraw_remove)
        pass
    elif choice == '3':
        print("\n Available Balance =", sum(transactions))
        pass
    elif choice == '4':
        print(transactions[-10:])
        pass
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
