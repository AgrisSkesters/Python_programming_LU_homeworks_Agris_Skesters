#1.

name = input("Enter first name: ")
surname = input("Enter last name: ")
print(name, surname)

#2.

text = input("Enter text: ")
output = text*3
print(output)

#3.

number = input("Enter number: ")
print(number+"+"+number*2+"+"+number*3+"="+str(int(number)+int(number*2)+int(number*3)))

#4.

radius = int(input("Enter radius: "))
height = int(input("Enter height: "))
volume = 3.14 * radius**2 * height
area = 2 * (3.14 * radius**2) + height * (2 * 3.14 * radius)
print("Volume: "+str(volume)+"\n"+"Area: "+str(area))

#5.

seconds = int(input("seconds: "))
hours = seconds // 3600
minutes = (seconds - hours*3600) // 60
finalSeconds = seconds - hours*3600 - minutes*60
print(str(hours)+" hours "+str(minutes)+" minutes "+str(finalSeconds)+" seconds")


