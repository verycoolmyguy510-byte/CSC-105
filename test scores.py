sName = input("PLease enter your name: ")

iTest1 = int(input("Test 1: "))
if iTest1 <= 0:
    print("\nTest scores must be greater than 0!")
    iTest1 = int(input("Test 1: "))
    if iTest1 <= 0:
        print("Test scores must be greater than 0!")
        raise SystemExit

iTest2 = int(input("Test 2: "))
if iTest2 <= 0:
    print("\nTest scores must be greater than 0!")
    iTest2 = int(input("Test 2: "))
    if iTest2 <= 0:
        print("Test scores must be greater than 0!")
        raise SystemExit

iTest3 = int(input("Test 3: "))
if iTest3 <= 0:
    print("\nTest scores must be greater than 0!")
    iTest3 = int(input("Test 3: "))
    if iTest3 <= 0:
        print("Test scores must be greater than 0!")
        raise SystemExit

iTest4 = int(input("Test 4: "))
if iTest4 <= 0:
    print("\nTest scores must be greater than 0!")
    iTest4 = int(input("Test 4: "))
    if iTest4 <= 0:
        print("Test scores must be greater than 0!")
        raise SystemExit


avg_all = (iTest1 + iTest2 + iTest3 + iTest4) / 4

lowest = iTest1
if iTest2 < lowest:
    lowest = iTest2
if iTest3 < lowest:
    lowest = iTest3
if iTest4 < lowest:
    lowest = iTest4

total = iTest1 + iTest2 + iTest3 + iTest4 - lowest
avg_drop = total / 3

if avg_all >= 90:
    grade_all = 'A'
elif avg_all >= 80:
    grade_all = 'B'
elif avg_all >= 70:
    grade_all = 'C'
elif avg_all >= 60:
    grade_all = 'D'
else:
    grade_all = 'F'

if avg_drop >= 90:
    grade_drop = 'A'
elif avg_drop >= 80:
    grade_drop = 'B'
elif avg_drop >= 70:
    grade_drop = 'C'
elif avg_drop >= 60:
    grade_drop = 'D'
else:
    grade_drop = 'F'

print("\n--- Results ---")
print(f"Average (all 4 tests): {avg_all:.2f}")
print(f"Letter Grade: {grade_all}")

print(f"\nAverage (lowest dropped): {avg_drop:.2f}")
print(f"Letter Grade: {grade_drop}")
# I liked the challenge this assignment offered. Well, it also kinda made me a little frusturated, as I struggled with most aspects of it but it was
# nice to get it done. I figured out how to drop the lowest grade by having the code start by assuming test 1 was the lowest grade. I then had the code
# compare the first test to the rest of the tests and if it finds a lower grade, it would replace test 1 and drop that test. And since there was 4 tests,
# with 3 that needed to be compared to the first, I knew to use 3 other if statements. Doing this assignment, I learned how to validate user input by checking if
# test scores were greater than zero and prompting the user again if they entered an invalid value. I also learned how to use if and elif statements to make decisions
# in my program, such as determining the lowest test score and assigning a letter grade based on the average score. I also learned how to calculate averages and how to
# modify calculations by dropping the lowest value before computing a final result.


