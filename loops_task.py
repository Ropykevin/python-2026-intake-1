# Write a program that displays a numbers 1 to 50 inside a list.
numbers=list(range(1,51))
# From 1 above display the ones divisible by 7 or 5 inside a list.
div=[]
for i in numbers:
    if i%7==0 or i%5==0:
        div.append(i)
print(div)

# Find sum and average of values in the range between 10 to 40.
numbers=list(range(10,41))
sum=0
for i in numbers:
    sum=sum+i

print(sum)
average=sum/len(numbers)
print(average)
# Put in a list the first 10 odd numbers between 10 to 50. 
numbers=list(range(10,51))
odd=[]

for i in numbers:
    if i%2==1:
        odd.append(i)
        if len(odd)==10:
            break
        

print(odd)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num=input('Enter a number:')
num=int(num)

numbers=list(range(11))
for i in numbers:
    mult=i*num
    print(f'{num}*{i}={mult}')
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop

numbers=list(range(1,51))
even=[]
for x in numbers:
    if x%2==0:
        even.append(x)
print(len(even))

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.

ls1 = [('Jay', '20'), ('Mo', '30'), ("Mya",'32') ,('xyz','100')]

total_quantity=0
for i in ls1:
    quantity=int(i[1])
    total_quantity=total_quantity+quantity
print(total_quantity)