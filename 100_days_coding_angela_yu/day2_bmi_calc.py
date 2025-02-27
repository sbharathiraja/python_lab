"""
BMI Calculator
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

bmi is equal to the person's weight divided by the person's height squared.

Convert this sentence into code on line 6.
"""

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
h_sqr = height**2
bmi = float(weight/h_sqr)

print(bmi)