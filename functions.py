#function can perform any task and it can reuse anytime
def printName():
    print("My function name is print")

#function
printName()

#argument function and parameter function

def myAge(age):
    print(" my age is ", age)

myAge(19)

#find the area of square using function.
def calculate_area_of_square(side_length):  
    return side_length * side_length  
  
side = int(input("Enter square's side length: "))  
area = calculate_area_of_square(side)  
print(f"The area of the square is: {area}")