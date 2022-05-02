# Write a program which will be displaed all Odd numbers within n
#Even2.py
n=int(input("Enter A Number :"))
if(n<=0):
    print("{} Is Invalid Input Plz Enter +ve Number".format(n))
else:
    i=1
    while(i<=n):
        print("{}".format(i),end="  ")
        i=i+2