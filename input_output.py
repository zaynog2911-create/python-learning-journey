import time

age=int(input("Please enter your age: "))
if age<18:
    print("You are still a minor.")
else:
    print("You are an adult. you can appply for driving licence, please fill the required information carefully.")
    name=input("Please fill the required information:\nName: ")
    address=input("Adress: ")
    phone=input("Phone number: ")
    print("please wait....")
    time.sleep(4)
    print("Verified...your driving licence will br post to your adress")
    
