import math

# Calculate LMTD

Cin=float(input("Enter the temperature of cold fluid entering the pipe in Kelvin :"))
Cout=float(input("Enter the temperature of cold fluid exiting the pipe in Kelvin :"))
Hin=float(input("Enter the temperature of hot fluid entering the pipe in Kelvin :"))
Hout=float(input("Enter the temperature of hot fluid exiting the pipe in Kelvin :"))

ch=int(input("Enter 1 if it is a parallel flow or 2 for counter flow : "))

def parallel(Cin,Cout,Hin,Hout):
    T1= Hin-Cout
    T2=Hout-Cin
    return (T1-T2)/math.log(T1/T2)

def counter(Cin,Cout,Hin,Hout):
    T1=Hin-Cin
    T2=Hout-Cout
    return (T1-T2)/math.log(T1/T2)

if ch==1:
    print("LMTD for Parallel flows is : ", parallel(Cin, Cout, Hin, Hout))

elif ch==2:
    print("LMTD for counter flow is : ", counter(Cin, Cout, Hin, Hout))

else :
    print("Enter a valid input ")



