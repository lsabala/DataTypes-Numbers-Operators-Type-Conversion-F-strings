# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#expect we live up to 90 years 
#1 year = 365 days
#1 year = 52 weeks
#1 year = 12 months

#print(type(age))
#65
ageInYears = 90 - int(age)

ageInDays = int(365 * ageInYears)
ageInWeeks = int(52 * ageInYears)
ageInMonths = int(12 * ageInYears)

print(f"You have {ageInDays} days, {ageInWeeks} weeks, and {ageInMonths} months left.")



