# Write the program which will be dislpayed odd numbers to Nth number by while loop
#EvenNo.py  1 3 5 7...19
print("=" * 50)
n=int(input("Enter Any Number :"))
if(n<=0):
    print("*" * 50)
    print("{} Invalid Input...! Plz Enter Any +ve Number.".format(n))
    print("*" * 50)
else:
    i=1
    print("-" * 50)
    print("\tOdd Numbers")
    print("-" * 50)
    while(i<=20):
        print("\t\t{}".format(i))
        i=i+2
    else:
        print("=" * 50)