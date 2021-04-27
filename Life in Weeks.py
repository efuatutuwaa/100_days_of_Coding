age = input("What is your current age? : \n")
years = 100 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {years} years, {months} months, {weeks} weeks and {days} days left!")