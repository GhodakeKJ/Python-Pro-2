#Generate Pattern Like 11 12 13... to 19 20 By Using while loop
print("="*50)
n=int(input("Enter a Number :"))
if(n<=0):
    print("-" * 50)
    print("{} It's...Invalid Input Plz Inter +ve Number".format(n))
    print("-" * 50)
else:
    i=11
    while(i<=20):
        print("{}".format(i))
        i=i+1
    else:
        print("="*50)