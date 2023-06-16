# BMI Calc
print('Plz enter your info')
weight=float(input('Enter your weight in KG: '))
height=float(input('Enter your height in M: '))
# Math func
bmi=round(weight/(height**2))
if bmi < 18.5:
  print(f'Your BMI is {bmi} you are underwight.')
elif 18.5<bmi<25:
  print(f'Your BMI is {bmi} you have a normal weigth.')
elif 25<bmi<30:
  print(f'Your BMI is {bmi} you are slightly overweight.')
elif 30<bmi<35:
  print(f'Your BMI is {bmi} you are obese.')
else:
  print(f'Your BMI is {bmi} you are clinically obese.')