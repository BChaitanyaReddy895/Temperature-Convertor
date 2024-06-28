print("Welcome to Temperature Converter designed by B Chaitanya Reddy\n")
print("For conversion from Degree celsius to Fahrenheit enter 1\n")
print("For conversion from Degree celsius to Kelvin enter 2\n")
print("For conversion from Fahrenheit to Degree celsius enter 3\n")
print("For conversion from Fahrenheit to Kelvin enter 4\n")
print("For conversion from Kelvin to Fahrenheit enter 5\n")
print("For conversion from Kelvin to Degree celsius enter 6\n")
user_choice=int(input("Enter your choice:"))
if(user_choice==1):
    celsius=float(input("enter temp in degree celsius:"))
    fahrenheit=(celsius*1.80)+32
    print("Temperature in Fahrenheit:",fahrenheit)  
elif(user_choice==2):
    celsius=float(input("enter temp in degree celsius:"))
    kelvin=celsius+273.15
    print("Temperature in Kelvin:",kelvin)
elif(user_choice==3):
    fahrenheit=float(input("enter temp in Fahrenheit:"))
    celsius=(5/9)*(fahrenheit-32)
    print("Temperature in Degree celsius:",celsius)
elif(user_choice==4):
    fahrenheit=float(input("enter temp in Fahrenheit:"))
    kelvin=((5/9)*(fahrenheit-32))+273.15
    print("Temperature in Kelvin:",kelvin)
elif(user_choice==5):
    kelvin=float(input("enter temp in Kelvin:"))
    fahrenheit=((kelvin-273.15)*(9/5))+32
    print("Temperature in Fahrenheit:",fahrenheit)
elif(user_choice==6):
    kelvin=float(input("enter temp in Kelvin:"))
    celsius=kelvin-273.15
    print("Temperature in Degree celsius:",celsius)
else:
    print("Invalid choice\n")


