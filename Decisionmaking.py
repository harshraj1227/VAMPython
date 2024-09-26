#we have to use if else condition for decision making in python
#check you are eliggible for voting or not
#get user input
bornYear= int(input("enter your born year"))
currentYear=int(input("enter current year"))

userAge = currentYear - bornYear
print("Your age is", userAge)

if userAge>18 and userAge<55:
    print("you'r eligible for voting")
elif userAge>55:
    print("you'r eligible for super vote dear")
else:
    print("you'r not eligible for voting dear")