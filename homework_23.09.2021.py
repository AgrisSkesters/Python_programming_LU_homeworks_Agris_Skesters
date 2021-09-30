#1.

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

print(str(number_1)+" + "+str(number_2)+" = "+str(number_1+number_2))
print(str(number_1)+" - "+str(number_2)+" = "+str(number_1-number_2))
print(str(number_1)+" / "+str(number_2)+" = "+str(number_1/number_2))
print(str(number_1)+" * "+str(number_2)+" = "+str(number_1*number_2))

#2.

phoneNumbers = {
    "Johny": 37124789011,
    "Ana": 37126025682,
    "Jonathan": 37125213377,
    "Rebeca": 37122996351
}
print() # empty line
print(phoneNumbers)

phoneNumbers["Johny"] = "Jonhy@gmail.com"
print(phoneNumbers)

phoneNumbers["Kristopher"] = 37123236499
print(phoneNumbers)

del phoneNumbers["Rebeca"]
print(phoneNumbers)

#3.

shoppingList = ["bread", "milk", "water", "milk", "milk", "butter", "milk", "bread"]
correctedShoppingList = list(dict.fromkeys(shoppingList))
print() # empty line
print(shoppingList)
print(correctedShoppingList)

#4.

print() # empty line
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Is "+str(a)+" bigger then "+str(b)+" ?")

if a > b:
    print(True)
else:
    print(False)

#5.

print() # empty line
rotationNumber = input("Enter number: ")
test_list = []
test_list.extend(rotationNumber)
x = len(test_list)
while x > 0:
    print(test_list[x-1], end="")
    x -= 1







