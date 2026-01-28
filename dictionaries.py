my_dict={
    'name':'Ropy Kevin',
    'age':25,
    'location':'Kiambu',
    'city':'Nairobi'
    
}

print(my_dict)
print(type(my_dict))

# displaying values in dictionaries 
print(my_dict['age'])

# adding new keys and values
my_dict['occupation']='Software Developer'
my_dict['id']=1234567
print(my_dict)
# add address
# updating values
my_dict['age']=30

# update location

# Remove items
# pop
my_dict.pop('age')
# popitem(removes the lst item)
my_dict.popitem()
# copy

x=my_dict.copy()
print(x)
# fromkeys
x=my_dict.fromkeys([1,2,3,4,5],'alex')
print(x)
# get
print(my_dict.get('name'))
# items

print(my_dict.items())
# keys
print(my_dict.keys())  
# values
print(my_dict.values())
# setdefault
my_dict.setdefault('occupation','student')
print(my_dict)
