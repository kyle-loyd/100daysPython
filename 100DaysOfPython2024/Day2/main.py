print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
each_pay = round(total * (tip / 100 + 1) / split, 2)
print(f"Each person should pay: ${each_pay}")
