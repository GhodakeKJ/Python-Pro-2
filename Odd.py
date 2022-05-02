#Displays nth odd number within n will be +ve
#Odd.py
print("="*50)
n=int(input("Enter A Number :"))
if(n<=0):
    print("-" * 50)
    print("{} Is Invalid Input ...Enter +ve Number".format(n))
    print("-" * 50)
else:
    i=1
    while(i<=n):
        print("-" * 30)
        print("\t \t \t{}".format(i))
        i=i+2
        print("-" * 30)
