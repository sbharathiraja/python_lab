"""

SAMPLE INPUT and OUTPUT
Welcome to the tip calculator!
What was the total bill? $
123
How much tip would you like to give? 10, 12, or 15? 
15
How many people to split the bill?
2
Each person should pay: $70.72

"""

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 15, 20 or custom?"))

def calc_tip(bill, tip):
    print(bill)
    print(tip)
    t = float(tip/100)
    tip_amt = t*bill
    total_bill = tip_amt+bill
    return(total_bill)

total = calc_tip(bill, tip_percent)
print(total)
  
try:
    bill_split = int(input("How many people to split the bill?: "))
    if bill_split != 1:
        each_pay = float(total/bill_split)
        print ("total amount for each person  = $", each_pay)
    else:
        print ("Your total = $", total)
except:
    print("Hmm, please enter a valid integer")
