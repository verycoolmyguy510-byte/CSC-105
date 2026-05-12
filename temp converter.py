
print("Welcome! This program was created by Liam McGrail.")

fTempEnteredLFM = float(input("Enter a temperature: "))

sTempTypeLFM = input("Is this Fahrenheit (F/f) or Celsius (C/c)? ")

if sTempTypeLFM not in ["F", "f", "C", "c"]:
    print("Enter a F or C")

elif sTempTypeLFM in ["F", "f"]:
    if fTempEnteredLFM > 212:
        print("Temp can not be > 212")
    else:
        fCelsiusLFM = (5.0 / 9) * (fTempEnteredLFM - 32)
        print(f"The Celsius equivalent is: {fCelsiusLFM:.1f}")

elif sTempTypeLFM in ["C", "c"]:
    if fTempEnteredLFM > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheitLFM = ((9.0 / 5.0) * fTempEnteredLFM) + 32
        print(f"The Fahrenheit equivalent is: {fFahrenheitLFM:.1f}")

 # I liked working with if/elif/else statements because it helped me understand how a program makes decisions based on user input.
 # I would say I struggled with getting the conditions right, especially making sure the program only accepts F or C and handles errors correctly.
 # An if/else statement is used when there are two possible outcomes. The program checks a condition, and if it is true, it runs the code under the if.
 # If the condition is false, it runs the code under the else. So it’s basically a yes/no decision. An if/elif/else statement is used when there are more
 # than two possible outcomes. The program first checks the if condition. If that is false, it moves to the elif (which means “else if”) and checks another
 # condition. It can have multiple elif statements. If none of the conditions are true, the else block runs at the end. I used an if/elif/else statement in
 # this assignment because there were multiple conditions to check. The program had to determine whether the user entered Fahrenheit, Celsius, or an invalid
 # input. Using elif allowed me to check each case separately in a clear and organized way instead of trying to handle everything with just an if/else.
 # Three things I learned was how to check user input to make sure it’s valid (only F or C) and how to stop the program or show an error message if the input is
 # incorrect and I practiced using if, elif, and else statements to control the flow of a program based on different conditions, like whether the temperature is
 # in Fahrenheit or Celsius.
