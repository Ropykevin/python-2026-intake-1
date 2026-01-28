students=('Alex','Jane','Mike','Mary','John')
print(type(students))
print(students)
print(students[1])

# mary
print(students[3])

# change mary to juma
# convert a tuple to a list using list()
students=list(students)
students[3]='Juma'#modify

# convert back to tuple using using tuple()
students=tuple(students)
print(students)

# add your name between alex and jane
students=list(students)
print(students)
students.insert(1, "Benah")
print(students)
students = (tuple(students))
print(students)