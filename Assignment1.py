#Area of Square
# Question: Calculate the area of a square.
side = int(input("side:"))
area = side*side
print("Area of a square :",area)

# # #calculate area of rectangle
l=int(input("length :"))
b = int(input(" breadth :"))
area = l*b
print("Area of Rectangle:",area)

# # #calculate the area of triangle
l = int(input("length:"))
b= int(input("breadth:"))
h = int(input("height:"))
area = (1/2)*l*b*h
print("Area of Triangle:",area)

# # #Perimeter of square
s = int(input("side"))
print("Perimeter of Square:",4*s)

# # #perimeter of Rectangle
l = int(input("length"))
b= int(input("breadth"))
p = 2 *(l+b)
print("Perimeter of Rectangle:",p)

# #Perimeter of Triangle
s1,s2,s3 = map(int,input("enter sides:").split())
p = s1+s2+s3
print("Perimeter of Triangle:",p)

# #Question: Break the total amount into denominations.
amount = int(input("enter amount:"))
a = amount // 1000
amount -= a*1000
b = amount //500
amount -= b*500
c = amount
print(f"1000:{a} 500:{b} Remaining:{c}")

# #Question : Convert seconds into Hours , Minutes and seconds
s = int(input("Total Seconds:"))
min = s //60
s -=min*60
hours = min // 60
min-=hours*60
c = s
print(f"hours:{hours} minutes:{min} seconds:{c}")

# #Question : Average of Marks (Maths , Physics, Chemistry)
maths,physics ,chemistry = map(int,input("enter sbujects marks:").split())
avg = (maths+physics+chemistry)/3
print("average Marks :",avg)


# #check Even or odd :
a = int(input("enter number:"))
if (a %2==0):
    print("even")
else :
    print("odd")    

# #. Divisible by 5 but Not by 10
a = int(input("enter number:"))
if a%5==0 and a%10!=0 :
    print("satisfy")
else :
    print("not satisfied")
    
# #Biggest Among Two numbers
a,b = map(int,input("enter values:").split())
if a>b:
    print(a,"is greater")
else:
    print(b,"is greater")

# #smallest among two numbers
a,b = map(int,input("enter values:").split())
if a<b:
    print(a,"is smaller")
else:
    print(b,"is smaller")


# #Divisible by 2,3,6
a = int(input("enter number:"))
if a%2==0 and a%3==0 :
    print("satisfied")
else :
    print("not satisfied")


# #Voting eligibility
a = int(input("enter age:"))
if a>=18:
    print("eligible to vote")
else : 
    print("not eligible")
    
# students pass if passed any one Sbuject 
maths , chemistry ,physics = map(int,input("enter marks:").split())
if maths>=35 or chemistry>=35 or physics>=35 :
    print("pass")
else :
    print("fail")
    
    
# #Student pass if passes any two subjects 
if (maths>=35 and physics>=35) or (physics>=35 and chemistry>=35) or (chemistry>35 and maths>=35):
    print("pass")
else: print("fail")

#Biggest among three numbers
a,b,c = map(int,input("enter values"))
if a>b and a>c: print(a,"is greater")
elif b>a and b>c : print(b,"is greater")
else:print(c,"is greater")

# #smallest Among three numbers
if a<b and a<c: print(a,"is smaller")
elif b<a and b<c : print(b,"is smaller")
else:print(c,"is smaller")

#check if the number is perfect square 
a = int(input("enter a number"))
for i in range(a):
    if a==i*i:
        print("perfect square")
        break
else :
    print("not a perfect Square")
    
# #Cars Required for Members (Max % per car )
n = int(input("Enter number of people"))
req = n//5
print("cars needed:",req)

#second Biggest number among Three number
a,b,c = map(int,input("enter values").split())
if c>a>b or b>a>c  :print("second largest:",a)
elif a>b>c or c>b>a  :print("second largest",b)
elif b>c>a or a>c>b:print("second largest",c)

 #leap year or not
n =int(input("enter a year"))
if n%400==0:print(n,"is leap year")
elif n%100==0:print("not a leap year")
elif n%4==0: print(n,"is leap year")
else: print("not a leap year")

