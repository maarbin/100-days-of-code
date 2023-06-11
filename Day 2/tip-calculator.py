total = float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

amount = round((total / people) * ((100 + percent)/100), 2)

print(f"Each person should pay: ${amount:.2f}")