print("Welcome to the Tip Calculator 💸")
bill = float(input("What is the total bill?: GHS "))
tip = int(input("How much tip would you like to give: 10,12 or 15? or enter a custom tip: "))
people = int(input("How many people are splitting the bill?: "))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person would pay : GHC {final_amount}")

