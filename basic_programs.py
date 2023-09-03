
class basic_funstions:
        
    def addition_of_numbers(first_number,second_number):
        result=first_number+second_number
        print("addition of two numbers is:",result)


    def multiplication_of_numbers(first_number,second_number):
        result=first_number*second_number
        print("multiplication of two numbers is:",result)

    def division_of_numbers(first_number,second_number):
        def float_division():
            result=first_number/second_number
            print("float division of two numbers is:",result)
        def floor_division():
            result=(first_number//second_number)
            print("Floor Division:", result)

    def substraction_of_numbers(first_number,second_number):
        result=first_number-second_number
        print("substraction of two numbers is:",result)

    def swapping_with_third_variable(first_number,second_number):
        third_variable = first_number   
        first_number= second_number
        second_number= third_variable
        print(f"First number: {first_number} , Second Number:{second_number}")

    def swapping_without_third_variable(first_number,second_number):
        result=first_number+second_number
        first_number=result-first_number
        second_number=result-second_number
        print(f"First number: {first_number} , Second Number:{second_number}")

    def area_of_a_triangle(base,height):
        area =(base * height)/2   
        print("Area of triangle :", round((area),2))

    def positive_or_negative(numb):
        if ((numb>0)):
            print(f"{numb} is positive")
        elif ((numb<0)):
            print( f"{numb}is negetive")
        else:
            print(f"{numb} is 0")

    def even_or_odd(numb):
        if (((numb%2)==0)):
            print(f"{numb} is Even ")
        else:
            print('{} is Odd'.format(numb))

    def largest_number_among_three(first_number,second_number,third_number):
        largest=(max((first_number, second_number,third_number)))
        if first_number==second_number and second_number == third_number:
            print("{} {} {}".format(first_number , second_number, third_number),"are equal" )
        else:
            print("{}".format(largest,"is Largest Number"))

    def leap_year(year):
        if(((year %4==0)&(year%100!=0))|(year%400==0)):
            print(f'{year} is Leap Year')
        else:
            print(f'{year} is Not A LeapYear ')


    def prime_number(numb):
        if numb==0|numb<0|numb==1:
            print("its not a prime number: ")
        else:
            for i in range(2,(numb//2+1)):
                if numb%i==0:
                    print("it is not prime number")      
            else:   
                print (f'{numb} Is Prime Number')

    def prime_number_in_interval(inter1,inter2):
        for i in range(inter1,inter2):
            if i==0|i<0|i==1:
                print("its not a prime number: ")
            else:
                for j in range(2,(i//2+1)):
                    if i%j==0:
                        break 
                else:   
                    print(f'{i} Is Prime Number')


    def factorial_of_a_number(number):
        if number < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif number == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range(1,number + 1):
                factorial = factorial*i
        print("The factorial of",number,"is",factorial)

    def fibbinocci_sequence(number):
        a=0
        b=1
        c=1
        while a<number:
            print(a)
            a=b
            b=c
            c=a+b
        
    def armstrong_number(num):
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

    def hcf(x,y):
        
        hcf=0
        if x > y:
                smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i 
        print("The H.C.F. is", hcf)

    def lcm(x,y):
        
        hcf=0
        if x > y:
                smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i 

        print("LCM=", ((x*y)//hcf))

    def palindrom(str1):
        
        str2=""
        length=len(str1)
        for i in range(length-1,-1,-1):
            str2+= str1[i]
        if str2==str1:
            print(str1,"it is palindrome")

    def addition_of_matrix():
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


    def multiplication_of_matix():


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

    def no_of_occurence_of_an_item (string1):
        x=string1.split(" ")
        dict={}
        for i in x:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        print(dict)

