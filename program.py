# #Age Counting
# bornYear= int(input("enter your born year"))
# currentYear=int(input("enter current year"))

# userage = currentYear - bornYear
# print("Your age is", userage)

# #Currency Conversion
# INR=int(input("enter no of USD "))
# conversion= 84*INR

# print("after conversion: ", conversion)

#create their first Python project to generate random 6 digit OTP
import random  

def generate_otp(length=6):  
     
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])  
    return otp  

if __name__ == "__main__":  
    otp = generate_otp()  
    print(f"Your OTP is: {otp}")