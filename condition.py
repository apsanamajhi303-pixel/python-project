a=int(input("Enter your age: "))

if(a>18):
    print("Your age is 18 plus")
elif(a==18):
    print("Your age is 18")
else:
    print("Your age is below 18")
print("This is the end of the program.")

#Find the greatest of four numbers entered by the user.
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=int(input("Enter a number: "))

if (a>b and a>c and a>d):
    print(a," is greatest number.")
elif(b>c and b>d and b>a):
    print(b, "is greatest number.")
elif(c>a and c>b and c>d):
    print(c, "is greatest number.")
else:
    print(d, "is greatest number.")


#Find whether a student passed or failed, needing 40% total and 33% in each of 3 subjects.
sub1=float(input("Enter marks: "))
sub2=float(input("Enter marks: "))
sub3=float(input("Enter marks: "))
percentage = (sub1+sub2+sub3)/3

if (percentage>40 and sub1>33 and sub2>33 and sub3>33):
    print("Passed.")
else:
    print("Failed.")

#Detect spam comments containing keywords like "buy now" or "click this".
comment = input("Enter a comment: ")

if "buy now" in comment or "click this" in comment:
    print("Spam comment detected.")
else:
    print("Not a spam comment.")


#Find whether a given username contains less than 10 characters.
username = input("Enter a username: ")

if len(username)<10:
    print("Username has less than 10 characters.")
else:
    print("Username has more than 10 characters.")

#Find out whether a given number is present in a list.
numbers = [10, 20, 30, 40, 50]

num = int(input("Enter a number: "))

if num in numbers:
    print("Number is present in the list.")
else:
    print("Number is not present in the list.")

#Calculate a sutdent's grade from marks:90+Ex, 80+A, 70+B, 60+C, 50+D, below F.
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: Ex")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

#Find out whether a given post is talking about "Harry".
post = input("Enter a post: ").lower()

if "harry" in post:
    print("The post is talking about Harry.")
else:
    print("The post is not talking about Harry.")
