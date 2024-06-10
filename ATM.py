class ATM:
    def __init__(self, balance):
        self.balance=balance

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit_money(self, money):
        self.balance +=money
        print(f"{money} is deposited. New balance: {self.balance}")

    def withdraw_money(self, money):
        self.balance -=money
        print(f"{money} is withdraw. Current Balance: {self.balance}")

    def run(self):
        while True:
            print("\n1. Check Balance.")
            print("2. Deposit.")
            print("3. Withdraw money.")
            print("4. Exit.")
            choice=int(input("Enter your choice: "))
            if choice==1:
                self.check_balance()
            elif choice==2:
                money=float(input("Add money: "))
                self.deposit_money(money)
            elif choice==3:
                deduct=float(input("Amount: "))
                self.withdraw_money(deduct)
            elif choice==4:
                print("exiting..........")
                break
            else:
                print("Invalid choice. Try Again.......")

atm=ATM(10000)
atm.run()
