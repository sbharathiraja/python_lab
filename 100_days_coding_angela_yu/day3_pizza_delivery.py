print("Welcome to Python Pizza Delivery System")
size = input("What size pizza do you want? S, M, L or XL:  ")
size = size.lower()
pepperoni = input("Do you want pepperoni on your pizza? :  ")
pepperoni = pepperoni.lower()
extra_cheese = input("Do you want extra cheese? Y or N:  ")
extra_cheese = extra_cheese.lower()

bill = 0
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25
elif size == 'xl':
    bill += 30
else:
    print("You have entered wrong input, please type s for small, m for medium, l for large and xl for exrta large")

if pepperoni == 'y':
    if size == 's':
        bill += 2
    elif size == 'm' or size == 'l':
        bill += 3
    else:
        bill += 4

if extra_cheese == 'y':
    if size == 's' or size == 'm' or size == 'l':
        bill += 1
    else:
        bill += 2

print(f"Your final prize for your pizza is: ${bill}")