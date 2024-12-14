# BMI Calculator
print("BMI Caluclator!")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your Body Mass Index is: ")
print(int(bmi))


