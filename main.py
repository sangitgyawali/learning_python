# Banking Program in Python

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to deposit"))

    if amount < 0:
        print("That's not a valid amount")

    else:
        return amount

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4):")

    if choice == '1':
        show_balance()

    elif choice == '2':
        balance += deposit()

    elif choice == '3':
        withdraw()

    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice")

print("Thank You! Have a nice day")
