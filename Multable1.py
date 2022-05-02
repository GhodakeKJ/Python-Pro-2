#multable1.py
n=int(input("Enter A Number :"))
if(n<=0):
    print("{} is Invalid input :".format(n))
else:
    print("-"*50)
    print(" mul Table For :{}".format(n))
    print("-"*50)
    i=1
    while(i<=10):
        print("\t{} X {}\t =\t{}".format(n,i,n*i))
        i=i+1
    else:
        print("="*50)
