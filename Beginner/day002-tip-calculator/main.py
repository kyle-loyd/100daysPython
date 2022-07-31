#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
from varname import nameof

def print_value_error_response(field, definition):
  print(f"Provided value for {field} is invalid. {definition}")

try:
  bill_definition = "Positive decimal values allowed only."
  bill = float(input("Total Bill: "))
except ValueError:
  print_value_error_response(nameof(bill), bill_definition)
  exit()

try:
  party_definition = "Positive, numeric, non-decimal values allowed only."
  party_size = int(input("Party Size: "))
except ValueError:
  print_value_error_response(nameof(party_size), party_definition);
  exit()

try:
  tip_definition = "Positive, numeric, non-decimal values allowed only."
  percent_tip = int(input("Enter % tip to be paid: ")) / 100
except ValueError:
  print_value_error_response(nameof(percent_tip), tip_definition)
  exit()

split = (bill * percent_tip) / party_size
print(f"Each person would pay: ${'{:.2f}'.format(split)}")