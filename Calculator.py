class calculator:
    def addition(self,x,y):
        return x + y

    def subtraction(self,x,y):
        return x - y

    def multiplication(self,x,y):
        return x * y

    def division(self,x,y):
        return x / y

    def end(self):
        back = input("Press '0' to go back or '00' to exit: ")
        if back == "0":
            print()
            obj.calculate()
        elif back == "00":
            print()
            print("Thank You ❤")
        else:
            print()
            print("Invalid input")
            obj.end()
            
    def calculate(self):
        print("Press '1' for addition")
        print("Press '2' for subtraction")
        print("Press '3' for multiplication")
        print("Press '4' for division")
        print()
        choice = input("Make a choice: ")
        if choice == "1":
            num1 = float(input("Enter any number: "))
            num2 = float(input("Enter any number: "))
            print(num1," ➕ ",num2," = ",obj.addition(num1,num2))
            obj.end()
        elif choice == "2":
            num1 = float(input("Enter any number: "))
            num2 = float(input("Enter any number: "))
            print(num1," ➖ ",num2," = ",obj.subtraction(num1,num2))
            obj.end()
        elif choice == "3":
            num1 = float(input("Enter any number: "))
            num2 = float(input("Enter any number: "))
            print(num1," ✖ ",num2," = ",obj.multiplication(num1,num2))
            obj.end()
        elif choice == "4":
            num1 = float(input("Enter any number: "))
            num2 = float(input("Enter any number: "))
            print(num1," ➗ ",num2," = ",obj.division(num1,num2))
            obj.end()
        else:
            print()
            print("❌, Try Again ❗❕")
            print()
            obj.calculate()
            
obj = calculator()
        
print("Press '1' for addition")
print("Press '2' for subtraction")
print("Press '3' for multiplication")
print("Press '4' for division")
print()
choice = input("Make a choice: ")
if choice == "1":
    num1 = float(input("Enter any number: "))
    num2 = float(input("Enter any number: "))
    print(num1," ➕ ",num2," = ",obj.addition(num1,num2))
    obj.end()
elif choice == "2":
    num1 = float(input("Enter any number: "))
    num2 = float(input("Enter any number: "))
    print(num1," ➖ ",num2," = ",obj.subtraction(num1,num2))
    obj.end()
elif choice == "3":
    num1 = float(input("Enter any number: "))
    num2 = float(input("Enter any number: "))
    print(num1," ✖ ",num2," = ",obj.multiplication(num1,num2))
    obj.end()
elif choice == "4":
    num1 = float(input("Enter any number: "))
    num2 = float(input("Enter any number: "))
    print(num1," ➗ ",num2," = ",obj.division(num1,num2))
    obj.end()
else:
    print()
    print("❌, Try Again ❗❗")
    print()
    obj.calculate()
        

