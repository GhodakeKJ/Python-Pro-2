# Prohram Which Displayed nth Number Of Multiplication of +ve n numbers
#Multip.py
print("="*50)
n=int(input("Enter A Number :"))
print("="*50)
if(n<=0):
    print("-" * 50)
    print("{} Is Invalid Input Plz Enter +ve Number.".format(n))
    print("-" * 50)
else:
    i=1
    while(i<=10):
        print("\t{} \tX \t{}\t =\t{}".format(n,i,i*n))
        i=i+1
print("="*50)