def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Input must be a positive numeric value")
        except ValueError:
            print("Input must a positive numeric value")
        
deposit = get_positive_float("What is the Original Deposit (positive value): ")
rate = get_positive_float("What is the Interest Rate (positive value): ")
months = int(get_positive_float("What is the Number of Months (positive value): "))
goal = get_positive_float("What is the Goal Amount (can enter 0 but not negative): ")

current_balance = deposit
monthly_rate = (rate / 100) / 12


for month in range(1, months + 1):
    interest = current_balance * monthly_rate
    current_balance += interest
    
    
    print(f"Month: {month:<3} Account Balance is: $ {current_balance:,.2f}")

    # I liked the input validation aspect of this assignment. It was like defensive programming. I struggled with
    # successfully creating the loop without haviong it continue forever. I was able to get the float values to
    # get stored, which signaled the loop to stop. A while loop runs as long as a condition is true, so it’s best
    # when you don’t know how many times the loop will run, whereas a for loop runs a set number of times or over a sequence,
    # so it’s best when you know how many iterations you need. I used while loops so if the input is correct it runs once, and
    # I used for loops was so the program knows how mnay times to repeat the math. There are 4 loops in my code. In this assignement
    # I learned the difference between for and while loops, I learned how to apply the accumulator pattern using a for loop, and I learned how
    # to build "bulletproof" code using input validation loops. 
