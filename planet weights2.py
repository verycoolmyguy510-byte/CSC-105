MERCURY = 0.38
VENUS = 0.91
MOON = 0.165
MARS = 0.38
JUPITER = 2.34
SATURN = 0.93
URANUS = 0.92
NEPTUNE = 1.12
PLUTO = 0.066

sName = input("What is your name: ")

fEarthWeight = float( input(f"{sName} what is your earth weight: "))

fMercury = fEarthWeight * MERCURY
fVenus = fEarthWeight * VENUS
fMoon = fEarthWeight * MOON
fMars = fEarthWeight * MARS
fJupiter = fEarthWeight * JUPITER
fSaturn = fEarthWeight * SATURN
fUranus = fEarthWeight * URANUS
fNeptune = fEarthWeight * NEPTUNE
fPluto = fEarthWeight * PLUTO

print(f"\nHello {sName}! Your weight is {fEarthWeight}. This is your weight on other planets: \n")

print(f"Mercury: {fMercury:10.2f} ")
print(f"Venus:   {fVenus:10.2f}" )
print(f"Moon:    {fMoon:10.2f}")
print(f"Mars:    {fMars:10.2f}")
print(f"Jupiter:  {fJupiter:10.2f}")
print(f"Saturn:   {fSaturn:10.2f}")
print(f"Uranus:   {fUranus:10.2f}")
print(f"Neptune:  {fNeptune:10.2f}")
print(f"Pluto:    {fPluto:10.2f}")

# Reflection: I enjoyed the rewarding feeling I got when I could succesfully run the module without getting a syntax error
# and accomplishing the assignment. I originally struggled with the formatting, only allowing my name and weight to be used
# for the planet calculations instead of allowing a user to input their own information, as the assignment intended. I used
# the f string function to align the outputs better which made them less of an eye sore and easier to read. Three things I
# learned in this assignment was how to write an f string, how to allow a user to input their information, and how sensitive the
# Python language is, and how one minor spelling error can mess up the whole program.

