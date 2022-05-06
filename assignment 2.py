                            #Assignment 2

#Q1
str1 = "Python is a case sensitive language"
#a
print("Length of the input string:", len(str1))
#b
reverse = str1[::-1]
print(reverse)
#c
str2 = "a case sensitive"
str3 = str2[:]
#d
str3 = str3.replace('a case sensitive','object oriented')
print(str3)
#e
index = str1.index('a')
print(index)
#f
str4 = str1.replace(' ','')
print(str4)


#Q2
name = "TUSHAR MEENA"
SID = 21107118
Dept = "Mechanical"
CGPA = 6.2

print(f"Hey, {name} Here! \nMy SID is {SID} \nI am from {Dept} and my CGPA is {CGPA}")


#Q3
a,b = 56,10
print(a&b)
print(a|b)
print(a^b)
print(a<<2,b<<2)
print(a>>2,b>>4)


#Q4
str1 = input("Enter a string:")
if 'name' in str1:
    print('Yes')
else:
    print("No")


#Q5
a = int(input("Enter triangle side 1:"))
b = int(input("Enter triangle side 2:"))
c = int(input("Enter triangle side 3:"))
e = a + b > c and a + c > b and c + b > a

match e:
    case True:
        print('Yes')
    case False:
        print('No')

#Q6

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = bin(a^b)     #convert new number to binary
d = c.count('1') #count the bits needed to be changed
print(d)






