

#addition of two numbers
first_number=5
second_number=6
result=first_number+second_number
print("addition of two numbers is:",result)


#multiplication of two numbers
first_number=5
second_number=6
result=first_number*second_number
print("multiplication of two numbers is:",result)


#divide two numbers
first_number=5
second_number=6
result=first_number/second_number #float division
print("Float Division:", result)

result=(first_number//second_number)#floor division
print("Floor Division:", result)


#substraction of two numbers
first_number=5
second_number=6
result=first_number-second_number
print("substraction of two numbers is:",result)


#swaping of two numbers with third variable
first_number=5
second_number=6
third_variable = first_number   
first_number= second_number
second_number= third_variable
print(f"First number: {first_number} , Second Number:{second_number}")


#swaping of two numbers without third variable
first_number=5
second_number=6
result=first_number+second_number
first_number=result-first_number
second_number=result-second_number
print(f"First number: {first_number} , Second Number:{second_number}")


#squareroot of a number 
num1=90.8
root= num1**(1/2)
print('Square root:',round(root,2))


#calculate the area of traingle
base=int (input ("Enter base:" ))
height= int ( input ('enter height:' ) )
area =(base * height)/2   
print("Area of triangle :", round((area),2))




#check if a number is postive or negative or 0
numb=float(input("Enter any number"))
if ((numb>0)):
    print(f"{numb} is positive")
elif ((numb<0)):
    print( f"{numb}is negetive")
else:
    print(f"{numb} is 0")


#check if a number is odd or even
numb = float(input("Enter any number "))
if (((numb%2)==0)):
    print("{numb} is Even ")
else:
    print('{} is Odd'.format(numb))



#find largest number among three numbers
first_number=int(input("enter 1st number: "))
second_number=int(input("enter second number: "))
third_number=int(input("enter third number: "))
largest=(max((first_number, second_number,third_number)))
if first_number==second_number and second_number == third_number:
    print("{} {} {}".format(first_number , second_number, third_number),"are equal" )
else:
    print("{}".format(largest,"is Largest Number"))


#check whether a year is leap year or not
year=int(input("enter the year"))
if(((year %4==0)&(year%100!=0))|(year%400==0)):
    print('{year} is Leap Year')
else:
    print('{year} is Not A LeapYear ')
    

#check prime number
numb=int(input('Enter Any Number: '))
if numb==0|numb<0|numb==1:
    print("its not a prime number: ")
else:
    for i in range(2,(numb//2+1)):
        if numb%i==0:
            print("it is not prime number")      
    else:   
        print (f'{numb} Is Prime Number')



#check prime number in a interval
inter1=int(input('Enter interval1 Number: '))
inter2=int(input('Enter interval2 Number: '))

for i in range(inter1,inter2):
    if i==0|i<0|i==1:
        print("its not a prime number: ")
    else:
        for j in range(2,(i//2+1)):
            if i%j==0:
                break 
        else:   
            print(f'{i} Is Prime Number')



#factorial of a number
#method1
number = int(input("enter the number")) 
factorial=1
while number>1 :
    factorial+=factorial*(number-1)
    number=number-1
print(factorial)
    
#method2
if number < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       factorial = factorial*i
   print("The factorial of",number,"is",factorial)


#fibbinocci sequence
number=int(input("enter the last value of sequence: "))
a=0
b=1
c=1
while a<number:
   print(a)
   a=b
   b=c
   c=a+b
   
 
#check whether given number is armstrong number or not
num=int(input("enter a number: "))
sum_of_digit=0
temp=num
while temp>0:
    reminder=temp%10
    sum_of_digit+=(pow((reminder),3))
    temp=temp//10

if (sum_of_digit)==num:
    print(num,' is armstrong number.' )    
else:
   print(num,"is not an Armstrong number")


#hcf or gcd of a number


x = int(input("enter a number: ")) 
y = int(input("enter a number: "))
hcf=0
if x > y:
        smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i 
print("The H.C.F. is", hcf)



#lcm of a number
x = int(input("enter a number: ")) 
y = int(input("enter a number: "))
hcf=0
if x > y:
        smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i 

print("LCM=", ((x*y)//hcf))


#check the string is palindrome or not?
str1="malayalam" #palindrome
str2=""
length=len(str1)
for i in range(length-1,-1,-1):
   str2+= str1[i]
if str2==str1:
   print(str1,"it is palindrome")
   


#add two matrices
# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)


# Program to multiply two matrices using nested loops
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)

