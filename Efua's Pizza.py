print("Welcome to Efua's Pizza 💚")
size = input("Please choose your pizza size: S,M or L \n")
add_pepperoni = input("Would you like pepperoni?: Y or N\n")
extra_cheese = input("Would you like extra cheese?: Y or N\n")
crust = input ("How do you like your crust: Thin or Thick?\n")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
     bill += 3
if extra_cheese == "Y":
    bill += 1
if crust == "Thin":
    bill += 3
elif crust == "Thick":
    bill += 5
print(f"Your final bill is ${bill}. Enjoy your pizza 🍕.")
