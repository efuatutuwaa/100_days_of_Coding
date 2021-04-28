print("Welcome to the commission calculator 😉")

gross_earnings = float(input("How much did you earn today?:"))
final_gross_earning= "{:.2f}".format(gross_earnings)
commission = int(input("What is the commission charge?:"))
commission_as_percent = commission/100
total_commission_amount = gross_earnings * commission_as_percent
final_commission_amount ="{:.2f}".format(total_commission_amount)
net_earnings = gross_earnings - total_commission_amount
final_net_earnings = "{:.2f}".format(net_earnings)

print(f"Your commission on GHC {final_gross_earning} is GHC {final_commission_amount}")
print(f"You get to keep GHC {final_net_earnings} as your net earning, after paying your commission.")