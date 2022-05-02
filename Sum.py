# Program which will be displayed nth number of sum n must be +ve number
#Sum.py
n=int(input("Enter A Number :"))
if(n<=0):
    print("{} Is Invalid Input Enter A +ve Number !".format(n))
else:
    print("-"*50)
    print("Natural Sum \t\tSquares \t\tCubes")
    print("-"*50)
    s,ss,cs=0,0,0
    i=1
    while(i<=n):
        print("\t{}\t\t\t\t{}\t\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("-"*50)
        print("\tSum Is:{}\tSquare Is:{}\tCube Is{}".format(s,ss,cs))
        print("="*50)