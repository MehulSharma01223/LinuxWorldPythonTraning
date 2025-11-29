balance = 5000
pin = 1234

attempts = 0   # count incorrect attempts

while attempts < 3:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        print("PIN correct!")
        print("Your balance is:", balance)

        amount = int(input("Enter amount to withdraw: "))
        
        if amount <= balance:
            balance -= amount
            print("Transaction successful!")
            print("New balance is:", balance)
        else:
            print("Insufficient balance!")

        break  # exit loop after successful login
    
    else:
        attempts += 1
        print("Incorrect PIN! Attempts left:", 3 - attempts)

# After 3 incorrect attempts
if attempts == 3:
    print("❌ Your account is blocked due to 3 incorrect PIN attempts.")
