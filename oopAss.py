class Calculator:
    def __init__(self) -> None:
        pass

    def add(self,x,y):
        print(f"Addition result of{x} and {y} = {x + y}")
    
    def subtract(self, x, y):
        print(f"Subtraction result of {x} and {y} = {x-y}")
    
    def multiply(self, x, y):
        print(f"Multiplication result of {x} and {y} = {x*y}")
    
    def divide(self, x, y):
        if y == 0:
            print("Error")
        else:
            print(f"Division result of {x} and {y} = {x/y}")
        
    def perform_operations(self):

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        Operation = input("______Enter operation______\n Enter(1,2,3 or 4)\n1.Addition\n2.Subtraction\n3.Multiplication\n4. Division. \n********\n")
        if Operation == "1":
          self.add(num1,num2)
        elif Operation == "2":
          self.subtract(num1,num2)
        elif Operation =="3":
          self.multiply(num1,num2)
        else:
          self.divide(num1,num2)


calculator1 = Calculator()
calculator1.perform_operations()