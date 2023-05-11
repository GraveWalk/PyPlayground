# This one is a good one and simple a BMI calculator
# You can calculate it by using some mathematics let your script do the heavy calculations.

# we will require the (weight in kg) and (height in m)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

# I used float because it is for decimal value not integers becasue height or weight both have some grams and mm
# Now we will need to calculate this
# Formula for BMI is weight / height ^ 2 
# Put this in python 

bmi = round(weight / height ** 2, 2)
# (**) is used for exponent to add power 
#i used round attribute to round the answer to 2 decimal points
#now just print this

print(f'Your bmi is {bmi}')

# I used f string here to print this 
# f string allows you to use any data type a string a integer a float any data type in just one ("",'') saves a lot of time trust me.
# Well we can even modify this using if statements so it gives a particular response. like cheering for a good weight and 
# Asking to go look for help if underweight or overweight.
# We'll do that later.
