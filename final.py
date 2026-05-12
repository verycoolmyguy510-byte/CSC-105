fAccountBalanceLFM = 0.0
lstTransactionHistoryLFM = []


def PromptForInput(strPromptLFM):
    while True:
        try:
            fAmountLFM = float(input(strPromptLFM))

            if fAmountLFM <= 0:
                print("Enter a number that is > 0")
            else:
                return fAmountLFM

        except ValueError:
            print("Enter a valid numeric value")


def Deposit():
    global fAccountBalanceLFM

    fDepositAmountLFM = PromptForInput("Enter deposit amount: ")

    fAccountBalanceLFM += fDepositAmountLFM

    lstTransactionHistoryLFM.append(
        f"Deposit            +${fDepositAmountLFM:,.2f}"
    )

    print(f"Deposit successful! New balance: $ {fAccountBalanceLFM:,.2f}")



def Withdraw():
    global fAccountBalanceLFM

    if fAccountBalanceLFM == 0:
        print("Balance is $0.00. Cannot withdraw.")
        return

    while True:
        fWithdrawAmountLFM = PromptForInput("Enter withdrawal amount: ")

        if fWithdrawAmountLFM > fAccountBalanceLFM:
            print("Withdrawal amount cannot exceed account balance.")
        else:
            break

    fAccountBalanceLFM -= fWithdrawAmountLFM

    lstTransactionHistoryLFM.append(
        f"Withdrawal         -${fWithdrawAmountLFM:,.2f}"
    )

    print(f"Withdrawal successful! New balance: $ {fAccountBalanceLFM:,.2f}")



def CheckBalance():
    print("\n==============================")
    print(f"Current Balance: $ {fAccountBalanceLFM:,.2f}")
    print("==============================\n")



def TransactionHistory():
    print("\n========================================")
    print("         TRANSACTION HISTORY")
    print("========================================")

    if len(lstTransactionHistoryLFM) == 0:
        print("No transactions available.")
    else:
        for strTransactionLFM in lstTransactionHistoryLFM:
            print(strTransactionLFM)

    print("========================================\n")



def InterestApplication():
    global fAccountBalanceLFM

    if fAccountBalanceLFM == 0:
        print("Balance is 0 and no interest will be calculated.")
        return

    fInterestRateLFM = PromptForInput("Enter annual interest rate (%): ")

    fInterestLFM = fAccountBalanceLFM * (fInterestRateLFM / 100 / 12)

    fAccountBalanceLFM += fInterestLFM

    lstTransactionHistoryLFM.append(
        f"Interest Applied   +${fInterestLFM:,.2f}"
    )

    print(f"Interest applied: $ {fInterestLFM:,.2f}")
    print(f"New balance: $ {fAccountBalanceLFM:,.2f}")



def ProduceStatement():
    strFileNameLFM = "LFMBankStatements.txt"

    with open(strFileNameLFM, "w") as objFileLFM:
        objFileLFM.write("========================================\n")
        objFileLFM.write("        BANK STATEMENT REPORT\n")
        objFileLFM.write("========================================\n\n")

        if len(lstTransactionHistoryLFM) == 0:
            objFileLFM.write("No transactions available.\n")
        else:
            for strTransactionLFM in lstTransactionHistoryLFM:
                objFileLFM.write(strTransactionLFM + "\n")

        objFileLFM.write("\n========================================\n")
        objFileLFM.write(f"Final Balance: $ {fAccountBalanceLFM:,.2f}\n")
        objFileLFM.write("========================================\n")

    print(f"Statement saved to {strFileNameLFM}")


print("Welcome to Liam's Python Mini Banking System")

while True:
    print("\n1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Calculate and Apply Interest")
    print("6. Exit")

    strOptionLFM = input("Choose an option (1-6): ")

    if strOptionLFM == "1":
        Deposit()

    elif strOptionLFM == "2":
        Withdraw()

    elif strOptionLFM == "3":
        CheckBalance()

    elif strOptionLFM == "4":
        TransactionHistory()

    elif strOptionLFM == "5":
        InterestApplication()

    elif strOptionLFM == "6":
        ProduceStatement()
        print("Thank you for using the banking system!")
        break

    else:
        print("Invalid option. Please choose 1-6.")


# While doing this project, I enjoyed learning how to build programs with functions and
# user interaction. I struggled most with formatting and validation because small mistakes
# could stop the program from working correctly. During this semester I learned
# about variables, loops, conditionals, functions, lists, and file handling in
# Python. I also learned how to use exception handling and input validation to
# make programs more reliable and user friendly. Previous assignments helped
# prepare me for this project because they taught me how to organize code, break
# problems into smaller parts, and use functions to keep programs clean and efficient.
# I practiced using loops and conditionals to control program flow and learned how to
# store and display information using lists. This project helped me combine everything
# I learned throughout the semester into one complete banking application that can process
# transactions, calculate interest, and create statement files.




