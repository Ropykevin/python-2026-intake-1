numbers={10,20,30,40,50 ,10,40,50}
print(numbers)

# set methods 
# .add() used to add items 
numbers.add(1000)

# remove(item)=>use to remove items in a set
numbers.remove(10)
# numbers.remove(90)
# discard(item) =>used to remove items in the set 
numbers.discard(20)
numbers.discard(90)
print(numbers)


# set()=>used to covert data structures to sets making items unique

numbers={10,20,30,40,50 ,10,40,50}
x={10,20,30,4,5}
y=numbers.difference(x)
print(y)
print(x)