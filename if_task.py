# 1.Take three inputs from a user, separately. Print the largest of the numbers.
num1=input('Enter First number:')
num2=input('Enter second number:')
num3=input('Enter third number:')

num1=int(num1)
num2=int(num2)
num3=int(num3)

if num1>num2 and num1>num3:
    print(f'{num1} is the largest')
elif num2>num1 and num2>num3:
    print(f'{num2} is the largest')
else:
    print(f'{num3} is the largest')





#    Hint: Determine what type of data is  is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”

temperature =input('Enter temperature: ')
temperature=float(temperature)

if temperature>30:
    print('the temperature is too high')
elif temperature>15:
    print('Normal temperature')
else:
    print('Cold temperature')

# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"

x=9
y=110

if x>=10 and x<=20 and y>100:
    print('conditions met')
else:
    print('conditions not met')

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

password=input('Enter Your password :')
correct_password = 'secret123'
if password == correct_password:
    print('Access  granted')
else:
    print('Access denied')

# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"


#  formatted strings
# =>use to dislay variables in a string

# welcome ivy

# name="Brian"
# print(f'welcome {name}')