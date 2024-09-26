# data Type is used to define the data in which form 

# int data type is used to store the numeric data type.
# Note:- In python we don't need to declare the data types.
# We just assign the value in variable.
# Variable can store any type of value with any type of data.
age = 20
name = "Harsh Kumar"
salary=2548.69
# how to pass a variable inside the print statement .
#we have 3 way to pass the variable in print statement.
#print("my name is " + name +"my salary "+ salary+ "and age is "+ age)
#It generate the Type error, reason string only concatenate  with string not int or other
#Solution 1:- replace + by ,when data is not string
print("my name is " + name +" my salary ", salary, "and age is ", age)
#Solution 2:- pass the variable in print statement with f{}.
print(f"my name is {name} my salary  {salary} and age is  {age}")
#Solution 3:- Typecast the data into
salaryString= str(salary)
ageString = str(age)
print("my name is " + name +"my salary "+ salaryString+ "and age is "+ ageString)

#To find the type of data we need to use type() function
print(type(name))
print(type(age))
print(type(salary))