fPV = float( input(f"What is your starting balance: "))
fRate = float( input(f"What is your interest rate: "))
fTime = float( input(f"What is your time in years: "))
iCompound = int( input(f"What is your compounding time: "))

fRate = fRate / 100

FV = fPV * (1 + fRate / iCompound) ** (iCompound * fTime)

print(f"\nYour future value is: ${FV:,.2f}")

# I liked how this assignment required more math, which did make me struggle more
# I found this to make the assignment more engaging. We had to use () in the formula
# because it makes sure python executes the formula properly. I learned how to
# implement mathematical formulas in Python using operators such as division,
# multiplication, and exponentiation, as well as to format output using f-strings.
# By using the format specifier :,.2f, I was able to display the result as a properly
# formatted currency value with commas and two decimal places. I also learned the importance of
# parentheses in math equations in python.
