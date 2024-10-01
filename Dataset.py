#create list, tuple, set, dict
#Add data pawan, manan, tanya, mukul
#delete pawan
#access all data
#Update mukul to mukul sharma 
# add manam and print the data

#list
student = ["pawan","manan","Tanya","mukul"]
student.pop(0)
print(student)
student[1]="Tanya bhardwaj"
student.append("ritu raj")
print(student)

#tuple
mytuple=("pawan", "manan", "tanya", "mukul")
mytupleList = list(mytuple)
mytupleList[2] = "Tanya Bhardwaj"
mytupleList.pop(0)
mytupleList.append("harsh kumar")
print(mytuple)

#set
myset={"pawan","manan","tanya","mukul"}
print(myset)
myset.remove("pawan")
myset.add("ritu raj")
print(myset)
#in set we cann't able to update

#dict
myinfo = {"name" : "Harsh kumar",
        "email" :"harshkumar276002@gmail.com",
        "mobile" : "7464084218",
        "Age" :19,}

for value in myinfo.values():
     print(value)
     
myinfo["name"] = "nikhil tomar"
myinfo["Age"] = 20
myinfo["mobile"]=8764584616

myinfo.update({"gender":"male"})

for value in myinfo.values():
      print(value)