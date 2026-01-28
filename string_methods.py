my_name="Ropy Kevin"
print(my_name.lower())#converts strings to lowecase 
print(my_name.upper())#converts strings to uppercase 
# print(my_name.center(4))
x="     strip method    "
print(x)
x=x.strip()#removes spaces on the string
print(x)
my_name = "Ropy Kevin"
my_name=my_name.replace("Kevin","Brian")
print(my_name)

x=x+' '+"alex"
print(x)

# clean first_name= "  aLEx   "  to "alex"
first_name = "  aLEx   "
first_name=first_name.strip()
first_name=first_name.lower()
print(first_name)

# clean sentense1="  pYthoN PROGramming    " to "JAVA PROGRAMMING"

sentense1 = "  pYthoN PROGramming    "
sentense1=sentense1.strip()
sentense1 = sentense1.replace("pYthoN","java")
sentense1=sentense1.upper()

print(sentense1)
# .count =>counts the number of apearance of a character

main="Python Programming"
print(main.count("P"))

# .split =>used to split strings with a specified character creates a list
main = "Python Programming is awesome"
print(main)
x=main.split()
print(x)
# len() =>used to count the number of characters in the string
print(len(main))

x = "hello"
print(x.isascii())