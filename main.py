#If the bill was $150.00, split between 5 people, with 12% tip. 
#Example: Each person should pay (150.00 / 5) * 1.12 = 33.6
print("Welcome to tip calculator")
food_bill = float(input("How much money does the food cost?\n $"))
people = input("How many people are there?\n ")
tip = int(input("What percentage are you willing to tip (Note: Do not write the % symbol. Just white the number) = 1, 5 or 10?\n"))
tip_percentage = tip / 100
total_tip = tip_percentage * food_bill
total_bill = total_tip + food_bill
bill_per_person = float(total_bill) / int(people)
solution = round(float(bill_per_person),2)
print(f"Each person should pay: ${solution}")                  