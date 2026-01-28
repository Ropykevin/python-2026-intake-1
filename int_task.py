# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57
temp = 56.8926
temp=round(temp)
print(temp)

# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89
temp = 56.8926
temp=round(temp,2)
print(temp)
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 
temp = 56.8926
temp=round(temp,3)
print(temp)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 
temp = 56.8926

#1.convert to a string 
temp=str(temp)
print(type(temp))
#2. slice 
slice_temp=temp[3:7]
print(slice_temp)#8926
#3. concat
final_temp = slice_temp[0]+'.'+slice_temp[1:4]
#4. convert to float 
final_temp=float(final_temp)
print(final_temp)
# NB: Use string  slice & concatenation, but have result as float 

# convert temp = 56.8926 to 5.6
temp = 56.8926
temp=str(temp)

# slice
new_temp=temp[0:2]#56

f_temp=new_temp[0]+'.'+new_temp[1]
f_temp=float(f_temp)
print(f_temp)

myname = "Ropy",'alex','brian'
print(type(myname))


