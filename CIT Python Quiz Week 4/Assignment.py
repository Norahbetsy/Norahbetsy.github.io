1# creat a 2-D arry and slice out the second number in the second column

import numpy as np

a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
print(a)
b = a[0:2, 0:3]
print(b)

2# write a python program to sort array elements in the asecending/decending order

n=int(input(“Enter size of array\n“))
arr=list(map(int,input(“Enter elements of array\n“).split()))
arr.sort(reverse=False) #arr.sort() also be used
print(“Ascending order array”)
print(*arr)
arr.sort(reverse=True)
print(“Descending order array”)
print(*arr)
Input:
Enter size of array
5
Enter elements of array
3 9 4 8 1

3# write a python program to find the maximum and minimum value in a given 2-D array

# import numpy library
import numpy
 
# creating a numpy array of integers
arr = numpy.array([1, 5, 4, 8, 3, 7])
 
# finding the maximum and
# minimum element in the array
max_element = numpy.max(arr)
min_element = numpy.min(arr)
 
# printing the result
print('maximum element in the array is: ',
      max_element)
print('minimum element in the array is: ',
      min_element)

4 #write a python program to input 5 subjects marks and calculate totalmark,
  #percentage and grade based on following criteria
  #percentage less than 50(Grade C)
  #percentage equal to 50 and less than 80 (Grade B)
  #percentage equal to 80 and more than 80 (Grade A)
 
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")

# write a python program to fetch only Email ID from text file which include following fields
# Name
# Mobile Number 
# Roll Number
# Email ID

import re 
mport pyperclip 
Alltext = pyperclip.paste() 
EmailRegex = re.compile(r'' 
[a_zA_Z0_9_.+]+ 
@ 
[a_zA_Z0_9_.+]+ ,re.VERBOSE) 
result = EmailRegex.findall(Alltext) 
pyperclip.copy(result) 

#6 write  function for checking the the speed of drivers this function should have one parameter speed

def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_speed(80)
points = 2



#7 write a function  called show_star (rows) if rows are five you should print the following

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")


#8   write a program which will all such numbers which are divisible by 7 but are not 
# a multiple of 5 between 2000 and 3200 (both included) the numbers obtained shouid be printed in a comma separated sequence on a single line.

import math 
 
lower = math.ceil(2000 / 7) 
upper = math.floor(3201 / 7) 
for i in range(lower, upper+1): 
    if (7 * i) % 5 != 0: 
        print(7 * i, end =' ') 
    else: 
        continue 


#9 write a program which accepts a sequence of comma- separated numbers from console and generate  a list and a tuple which contains every number suppos the following input is supplied to the program 34,67,55,33,12,98 then the output should be


numbers = input("Type in numbers seperated only by a comma :")
numbers_split = numbers.split(',')

number_tuple = tuple(numbers_split)

print(number_tuple)
print(numbers_split)


#10 write a program the calculator and print the values according to the given formula Q=sequre root of [2*C*D)/H] following are the fixed values of  C AND H C=50 H=30 D is a varible whose values should be input to your program

import math
C=50
H=30
value = []
items=[x for x in input().split(',')]
for D in items:
    value.append(str(int(round(math.sqrt(2*C*float(D)/H)))))

print(','.join(value))



#11 write a function to compute 5/0 and use try /excep to catch the exceptions
def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception, err:
    print ('Caught an exception')
finally:
    print ('In finally block for cleanup')

#12 create a nesting list that prints out the color and the car brand

colors = [['Red'], ['Green'], ['Black']]
car brand = [['benze'], ['subaru'], ['marcardz']]

print('\n'.join([str(lst) for lst in colors]))
print('\n'.join([str(lst) for lst in car brand]))


#13 bonus question algorithm challange create your own sorting algorithm

count vowels:
stoped = False
while not stoped:
def count_vows():
word = input("Enter a word: ")
vows = 0
if " " in word:
print("Error, multiple words.")
stoped = True
else:
for letter in word:
if letter in "aeiou":
vows = vows + 1
vows = str(vows)
print("The word you entered has " + vows + " common vowels.")
stoped = True
count_vows()
