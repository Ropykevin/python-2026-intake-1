my_list=['mangoes','oranges','bananas',100,200,500,[1,2,['alex','mike'],3,4],True,False]
print(my_list[0])
print(type(my_list))
print(my_list[3:6])

print(my_list[6])
print(my_list[6][2][1])


content=['mon','tue',['jan','feb','may'],'wed',['nov','oct','dec'],'thur','fri']

print(content[2][1])
# may
print(content[2][2])
# oct
print(content[4][1])

# update items in a list
# we use index 
content = ['mon','tue','wed','thur','fri']

content[4]='friday'
print(content)
content[0]='Monday'
print(content)

content[3]='Thursday'
print(content)
        # list methods 
# len() function=>
content = ['MON', 'Tue','wed','thur','fri']
content.sort()
print(len(content))
# append() =>used to add an item at the end of the list
# content.append('sat')
print(content)
# insert()=>adds an item at a specified index
content.insert(1,'jan')
print(content)
# sort() sorts the list in a certain order
vowels=['a','i','u','o','e']
numbers=[10,5,6,90,50,1]
vowels.sort()
numbers.sort(reverse=True)
print(numbers)
# clear() =>clears all items in a list
numbers.clear()
print(numbers)
# extend() extends a list with another list
vowels = ['a', 'i', 'u', 'o', 'e']
numbers = [10,5,6,90,50,1]
vowels.extend(numbers)
print(vowels)

# pop())=>used to remove an  within a list if given index is give it removes the element on that index if not given it removes the lat element
numbers = [10, 5,6,90,50,1]
numbers.pop(2)
numbers.pop()
print(numbers)

#remove() removes a specified item 
numbers = [10, 5, 6,90,50,1]

numbers.remove(50)
print(numbers)

# count(item) counts the appearance of an item in alist
numbers = [10, 5, 6, 90,50,1,50]

print(numbers.count(50))

# copy returns a shallow copy
x=numbers.copy()
print(x)

# reverse (reverses the list)
numbers.reverse()
print(numbers)

# membership (in) check if an item is in a list
numbers = [10, 5, 6, 90, 50,1,50]
del numbers[1]
print(10 in numbers)