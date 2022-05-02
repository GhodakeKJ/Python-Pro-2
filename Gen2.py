#generat a Python Program Which will be 1 to nth numbers where n must be +ve
#Gen2.py
print("="*50)
n=int(input("Enter A Number :"))
if(n<=0):
    print("{} Is Invalid Input Plz Enter +ve Number !".format(n))
else:
    i=1
    while(i<=n):
        print("{}".format(i),end="   ")
        i=i+1
