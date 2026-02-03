def hello(name):
    print(f'hello {name}!')

hello('Alex')
hello('Brian')
hello('Maggie')

# calculate the area of a triangle
# base=10
# height=12
# area=0.5*base*height
# print(area)

def area_triangle(base,height):
    area = 0.5*base*height
    print(area)
    
area_triangle(10,12)
area_triangle(15,20)
area_triangle(5,15)

# calculate area of a circle 

# without function 


# with functions 

def area_circle(r):
    pie=3.14
    area=pie*r*r
    print(area)

area_circle(7)
area_circle(10)
area_circle(30)

# create a function that check if a number is even or odd
# num=10
# if num%2==0:
#     print('even')
# else:
#     print('odd')

def check_number(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

check_number(10)
check_number(11)