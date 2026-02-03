# 3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# Prints "Access Granted" if user_id is in valid_ids.
# Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105


if user_id in valid_ids:
    res='Access Granted'
else:
    res='Access Denied'
    
print(res)
# 4.Given a variable value that could be of any type, write a conditional statement that:
# Prints "String Detected" if value is a string.
# Prints "Integer Detected" if value is an integer.
# Prints "Unknown Type" for any other type.

value='1000'

if type(value)==int:
    val='interger detected '
elif type(value)==str:
    val='String Detected'
else:
    val='Unknown type'

print (val)


# if condition1:
    # code block for condition1
    # if condition2:
        # code block for condition2
    # else:
        # code block for the else case of condition2
# else:
    # code block for the else case of the condition1 if statement
    
age=30
# checks age of a person if age >18 allow access then we check if age >22 Drink 

if age>18:
    print('Allow access')
    if age >22:
        print('Drink')
    else:
        print('dont drink')
else:
    print('deny access')


1.# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
age =input('Enter your age: ')
age=int(age)
if age>=18:
    license=input('Do you have a drivers license yes/no:')
    if license=='yes':
        print('Eligible to drive ')
    else:
        print('Not Eligible to drive')
else:
    print('You are too young to drive')
    
2.  # Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."
credit_score=input('enter the credit score: ')
anual_income=input('enter anual income: ')
credit_score=float(credit_score)
anual_income=float(anual_income)
if credit_score>700:
    if anual_income>50000:
        print('Loan approved')
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")
