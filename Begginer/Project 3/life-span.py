# This is another project using some mathematics
# In this we are considering a person max life is 90 years
# Our objective is to calculate how many days,weeks,months,year arey left for that person if his max life is 90

age = int(input("Enter your age: "))
max_life = 90

# we have a varibale which will ask for user age
# we have a variable which defines max life to be 90 years.

years_left = max_life - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {years_left} years, {months_left} months ,{weeks_left} weeks ,{days_left} days left")

# I used f string to print all the data sets together
