print("Welcome to the Rollercoaster Ride, Stand by the scale to measure your height")
height = int(input("What is your height in cm?  "))

if height >= 120:
    print("You can enjoy the ride")
    age = int(input("Enter your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif 12 <= age < 18:
        bill = 7
        print("Youth ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")
    want_picture = input("Do you want a photo? Type  yfor Yes ad n for No. ")
    if want_picture == 'y':
        bill += 3

    print (f"Your total bill = {bill}$")

else:
    print("I am sorry you are not tall enough to take the ride")