#create a login system where thte user has three attempts to enter the correct username and password . If the user enters the wrong credentials three times, the account is locked. Use a while looop to manage the attempts and if-else statements to check the credentials .

# Predefined correct username and password
correct_username = "saim1234"
correct_password = "1234"

# Maximum number of attempts
max_attempts = 3
attempts = 0
account_locked = False

while attempts < max_attempts and not account_locked:
    # Get the username and password from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Check if the entered username and password are correct
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left.")
        
        # Check if the maximum number of attempts has been reached
        if attempts == max_attempts:
            account_locked = True
            print("Account locked due to too many failed login attempts.")

if account_locked:
    print("Please contact customer support to unlock your account.")
