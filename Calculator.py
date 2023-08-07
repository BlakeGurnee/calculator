print("This is a calculator input 2 numbers and it will calculate it.");
print("Do you want to add, subtract, divide, or multiply?");
i = input();
print("First Number: ");
j = input();
print("Second Number: ");
l = input();

if (i == "multiply"):
    print(float(j) * float(l));


elif (i == "divide"):
    print(float(j) / float(l));


elif (i == "subtract"):
    print(float(j) - float(l));


elif (i == "add"):
    print(float(j) + float(l));
    
else:
    print("Error")
    
input()
input()
print("Hello welcome to the secret menu");
print("Do you want to find the area or circumference of a circle? y/n");
k = input();

if(k == "y"):
    print("Ok enter first number: ")
    j = input();
    print("Are you trying to find area y/n");
    m = input();
    if(m == "y"):
        print(int(j) * int(j) * 3.14);
    elif(m == "n"):
        print(int(j) * 3.14);
        
elif(k == "n"):
    print("Bye!!!");
        
    
        







