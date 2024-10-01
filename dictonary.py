#dictonary is the used for key value pair
# eg. name : harsh kumar
# Feature:  ---->Ordered
#           ---->No duplicate
#           ---->changeable
# Syntax :- 
myinfo = {"name" : "Harsh kumar",
        "email" :"harshkumar276002@gmail.com",
        "mobile" : "7464084218",
        "Age" :19,}
#To access special data from dictionary
#syntex:- dict["key"]

# print(myinfo["mobile"])

# print("My name is ",myinfo["name"], "My age is",myinfo["Age"],"My email ID is",myinfo["email"],"My mob. no. is ",myinfo["mobile"])

# # acces the complete dictionary key value 

# for value in myinfo.keys():
#     print(value)

# # To modify the data store in dictionary
# dict["key"] = "change value"
myinfo["name"] = "nikhil tomar"
myinfo["Age"] = 20
myinfo["mobile"]=8764584616

# for value in myinfo.values():
#      print(value)
# add the new key
myinfo.update({"gender":"male"})

#myinfo.pop("email")
del myinfo["email"]
for value in myinfo.values():
      print(value)