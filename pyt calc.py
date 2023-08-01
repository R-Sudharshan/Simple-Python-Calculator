print("Welcome to the new Python Calculator")
print("Enter your values and then enter the operation for instant and accurate answers")


a = int(input("First no.:"))
b = int(input("Second no.:"))
operation = input("1.add,2.subtract,3.Multiply,4.Divide\n")
if(operation =="1" or "add"):
   print(a+b)
elif(operation == "2" or "subtract"):
     print(a-b)
elif(operation == "3" or "multiply"):
     print(a*b)
elif(operation == "4" or "divide"):
     print(a/b)

