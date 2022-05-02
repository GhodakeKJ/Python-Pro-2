#NumGen1.py Generate 1 2 3 4 5 6 7 8 9 10
print("=" * 50)
n=int(input("Enter Any  Number :"))
if(n<=0):
    print("*" * 50)
    print("{} Is Invalid Input".format(n))
    print("*" * 50)
else:
    i=1
    while (i<=10):
        print("\t \t {}".format(i), end=" ")
        i=i+1
