fruits = ['Mangoes', 'bananas', 'oranges', 'lemon','xyz']

for i in fruits:
    print(i)
    

x=[1,2,3,4,5,6,7,8,9,10]

for i in x:
    print('Alex')

# range() ->used to create a list of numbers 

numbers=list(range(1,101))
print(numbers)
for i in numbers:
    print('Alex')

# create a list of numbers from 10 to 50
# print your name 40 times
numbers = list(range(10, 51))
even_numbers=[]
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
        
print(even_numbers)

# display odd numbers 


numbers = list(range(10, 51))
odd_numbers=[]
for num in numbers:
    if num % 2 !=0:
        odd_numbers.append(num)

print(odd_numbers)


# break used to stop a loop
numbers=list(range(1,1000))
for i in numbers:
    print(i)
    if i == 30:
        break
    
    
numbers=list(range(1,4))
for i in numbers:
    pin=input('enter pin:')
    correct_pin='5496'
    if pin==correct_pin:
        print('Access granted')
        break
    else:
        print('try again')