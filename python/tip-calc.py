print("Welcome to the tip clacluator!")
bill =float(input ("Enter your total bill?£"))
tip =int(input("how much tip would you like to give? 10, 12 or 15?"))
people = int(input("how many people are paying?"))

tip_as_percent = tip / 100
total_tip_amount= bill * tip_as_percent 
total_bill= bill + total_tip_amount
total_per_person= total_bill / people 
final_amount = round(total_per_person,2)
print(f"total amount for your bill for each person would be:£{final_amount}")
