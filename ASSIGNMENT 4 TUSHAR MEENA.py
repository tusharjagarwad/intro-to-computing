#Assignment 4
#Name: TUSHAR MEENA
#SID: 21107118
#Branch: Mechanical
print("Q1")
while True:

    mark = int(input("Enter mark:"))
    if mark < 25:
        print("Grade: F")
    elif 25 <= mark < 45:
        print("Grade: E")
    elif 45 <= mark < 50:
        print("Grade: D")
    elif 50 <= mark < 60:
        print("Grade: C")
    elif 60 <= mark < 80:
        print("Grade: B")
    elif mark >= 80:
        print("Grade: A")


print('Q2')
year = int(input('Enter year:'))
if year % 4 == 0:
    if year % 100 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year")

print('Q3')
import random

for i in range(1,11):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    ans = int(input(f'Question {i}:{a}x{b}='))
    if ans == a*b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a*b)

print('Q4')
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("Answer:",i)