height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100) ** 2

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a healthy weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are severely obese.")
