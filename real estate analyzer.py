def getFloatInput(strPromptTextLFM):

    while True:

        try:
            fValueLFM = float(input(strPromptTextLFM))

        
            if fValueLFM <= 0:
                print("ERROR: Value must be greater than zero.")
            else:
                return fValueLFM

        except ValueError:
            print("ERROR: Please enter a valid numeric value.")


def getMedian(lstValuesLFM):

    intCountLFM = len(lstValuesLFM)

    if intCountLFM % 2 == 1:

        intMiddleLFM = intCountLFM // 2
        return lstValuesLFM[intMiddleLFM]

    else:

        intMiddleLFM = intCountLFM // 2

        fMedianLFM = (
            lstValuesLFM[intMiddleLFM] +
            lstValuesLFM[intMiddleLFM - 1]
        ) / 2

        return fMedianLFM


lstSalesValuesLFM = []

while True:

    fSalesPriceLFM = getFloatInput("Enter property sales value: $")

    lstSalesValuesLFM.append(fSalesPriceLFM)

    while True:

        strContinueLFM = input(
            "Enter another value? Y or N: "
        ).upper()

        if strContinueLFM == "Y":
            break

        elif strContinueLFM == "N":
            break

        else:
            print("ERROR: Please enter Y or N.")

    if strContinueLFM == "N":
        break
    
lstSalesValuesLFM.sort()

print("\n--- Sorted Sales Values ---")

for fValueLFM in lstSalesValuesLFM:
    print("${:,.2f}".format(fValueLFM))


fMinimumLFM = min(lstSalesValuesLFM)
fMaximumLFM = max(lstSalesValuesLFM)
fTotalLFM = sum(lstSalesValuesLFM)
fAverageLFM = fTotalLFM / len(lstSalesValuesLFM)
fMedianLFM = getMedian(lstSalesValuesLFM)
fCommissionLFM = fTotalLFM * 0.03


print("\n--- Sales Statistics ---")

print("Minimum:   ${:,.2f}".format(fMinimumLFM))
print("Maximum:   ${:,.2f}".format(fMaximumLFM))
print("Total:     ${:,.2f}".format(fTotalLFM))
print("Average:   ${:,.2f}".format(fAverageLFM))
print("Median:    ${:,.2f}".format(fMedianLFM))
print("Commission:${:,.2f}".format(fCommissionLFM))

# While I worked on this assignment, I liked learning how to use loops and functions together
# to organize a program and make it easier to read. However, I felt I struggled with validating
# the user input and making sure the loops repeated correctly when bad data was entered.
# A list stores multiple values in one variable. Each item has a position called an index,
# and lists can be sorted, updated, or looped through. A list could be used to store clothing
# product prices for an online store project so totals and averages can be calculated.
