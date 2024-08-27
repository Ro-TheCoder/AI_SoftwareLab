Fe=55.845
S=32.065
O=16

while True :
    amount=float(input("How much SO3 is produced in kg ? "))
    moles1=amount/(S + 3*O)
    ch=int(input("Enter 1 to get amount of FeS2 and 2 to get amount of required O2"))
    if ch==1:
        moles2=moles1/2
        amount2=moles2*(Fe+2*S)
        print("The amount of FeS2 used is ",round(amount2,3))
    elif ch==2:
        moles2=moles1*15/8
        amount2=moles2*2*O
        print("The amount of O2 used is ",round(amount2,3))
    else:
        print("Enter valid input")
