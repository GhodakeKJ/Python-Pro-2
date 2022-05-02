# program which will be displayed nth even numbres n must be +ve number
#Even.py
print("="*50)
n=int(input("Enter A Number :"))
print("="*30)
if(n<=0):
    print("{} Is Invalid Input...Enter +ve Number !".format(n))
else:
    i=0
    while(i<=n):
        print("\t\t\t{}".format(i))
        i=i+2
        print("=" * 30)
print("="*50)