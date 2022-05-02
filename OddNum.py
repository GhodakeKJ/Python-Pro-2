# Write a program which will be displayed nth Even numbers within n
#OddNum.py
n=int(input("Enter A Number :"))
if(n<=0):
    print("{} Is Invalid Input Plz Enter Any +ve Number...!".format(n))
else:
    i=0
    while(i<=n):
        print("{}".format(i),end="  ")
        i=i+2