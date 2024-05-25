class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.attempts = 0
        self.locked = False

    def login(self, entered_password):
        if self.locked:
            print("Account locked. Please contact admin.")
            return False
        if entered_password == self.password:
            print("Login successful!")
            self.attempts = 0
            return True
        else:
            self.attempts += 1
            if self.attempts >= 3:
                self.locked = True
                print("Too many wrong attempts. Account locked.")
            else:
                print(f"Wrong password. {3 - self.attempts} attempts left.")
            return False

# Example usage:
user = User("username", "password123")

for _ in range(4):
    entered_password = input("Enter password: ")
    if user.login(entered_password):
        break
