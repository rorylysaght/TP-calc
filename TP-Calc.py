# Count how much Toilet Paper you have stockpiled
# Rory MacLysaght rorylysaght@gmail.com
#
# This is a work in progress - there is currently no data validation or sanitization - use at your own risk
# Not approved by CDC, FDA, USDA or American TP Association
from os import system
import textwrap
# define our clear function
def clearScreen():
    system('clear') # NB: If on Windows, change this line to: system('cls')

# Current default type for multipurpose Apocalypse calculator
freakout = "Coronavirus"
# How many sheets in average roll of TP
numPerRoll = 400
# How many sheets per wipe
numPerWipe = 10
# Avg Poops per day
ppd = 1
# Persons in household
numHousehold = 2

# Maybe it's a different emergency, but default to Corona
currFreakout = input("What is the current crisis? ").title() or freakout

clearScreen()

# Construct our banner
banner = "*" * 55 + '\n'
banner += " " * 15 + currFreakout + " Apocalypse"+ '\n'
banner += " " * 15 + "Toilet Paper Calculator"+ '\n'
banner += "*" * 55 + '\n'

print(banner)

print("First, a few questions to determine your status.")
print("To accept the normal defaults, just hit return." + '\n')

myHousehold = input("How many people in your household (default " + str(numHousehold) + ")? ") or numHousehold
myNumPerWipe = input("Average number of sheets used per wipe (default " + str(numPerWipe) + "): ") or numPerWipe

# NOTE: Need to add data input validation and sanitization here
# Assuming good intent and valid integer entries for now
# Here's the complicated math:
wipesPerRoll = (numPerRoll / int(myNumPerWipe)) / ppd
daysPerRoll = wipesPerRoll / int(myHousehold)

daysPerRoll = round(daysPerRoll)

clearScreen()

print(banner)

strOutput = "Studies have shown that 98% of people poop between three times per day to three times per week. "
strOutput += "An average roll of toilet paper has " + str(numPerRoll) + " sheets (according to Consumer Reports). "
strOutput += "Conservatively assuming each person in your household poops just once per day, "
strOutput += "and uses " + str(myNumPerWipe) + " sheets per visit, "
strOutput += "you can expect an average roll of TP to last about " + str(daysPerRoll) + " days."

print(textwrap.fill(strOutput, width=55) + '\n')

numRolls = input("How many rolls do you have stockpiled? ") or 1

# More complicated math:
daysLeft = round(daysPerRoll * int(numRolls), 1)
if daysLeft > 366:
    strDaysLeft = str(round(daysLeft/365)) + " years and " + str(daysLeft%365)
elif daysLeft > 30:
    strDaysLeft = str(round(daysLeft/30)) + " months and " + str(daysLeft%30)
else:
    strDaysLeft = str(daysLeft)

if daysLeft < 7:
    bioBanner = "%" * 55 + '\n'
    bioBanner += " BIO-HAZARD" * 5 + '\n'
    bioBanner += "%" * 55 + '\n'
    print(bioBanner)
    print("WARNING: You have less than " + str(daysLeft) + " days before reaching")
    print("         catastrophic TP levels.")
    if wipesPerRoll > 20:
        print("RECOMMENDATION*: Consider immediately reducing your")
        print("         current " + str(myNumPerWipe) + " sheets used per wipe!" + '\n')
        print("* This has not been approved by the CDC and should")
        print("  not be considered medical advice." + '\n')
else:
    okBanner = "*" * 55 + '\n'
    okBanner += " " * 22 + "DON'T PANIC" + '\n'
    okBanner += "*" * 55 + '\n'
    print(okBanner)
    print("You can last for about " + strDaysLeft + " days." +'\n')
    if int(numRolls) > 25 and int(myHousehold) < 3:
        hoarderBanner = "BUT SERIOUSLY PEOPLE! "
        hoarderBanner += "You have " + str(numRolls) + " rolls for " + str(myHousehold) + " people. "
        hoarderBanner += "How about you bring some of those unopened packs back to the store!" + '\n'
        print(textwrap.fill(hoarderBanner, width=55) + '\n')

print("Sources:")
print("https://www.healthline.com/health/how-many-times-should-you-poop-a-day")
print("https://www.consumerreports.org/cro/magazine/2015/08/the-dirty-little-secrets-of-toilet-paper")
print('\n')


# SOURCES:
# https://www.consumerreports.org/cro/magazine/2015/08/the-dirty-little-secrets-of-toilet-paper/index.htm
# https://www.healthline.com/health/how-many-times-should-you-poop-a-day
#
# (c)2020 Rory MacLysaght
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# <https://www.gnu.org/licenses/>.
