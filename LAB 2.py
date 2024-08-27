def mole(volume):
    result = (3.63 * volume) / (0.08205 * 303)
    return result


def partial(n):
    return round(((n/sum) * 2760),3)

def flow(a,b,c):
    a=a*16
    b=b*28
    c=c*2
    return round((a+b+c)/1000,2)


vol = int(input("Enter the volume of gas mixture : "))
Ch4 = int(input("Enter the Composition % of CH4 : "))
C2h6 = int(input("Enter the Composition % of C2H6 : "))
H2 = int(input("Enter the Composition % of H2 : "))

moleCh4 = mole(Ch4 * vol / 100)
moleC2h6 = mole(C2h6 * vol / 100)
moleH2 = mole(H2 * vol / 100)

sum = moleC2h6 + moleCh4 + moleH2

print()
print("Mole fraction of each component : ")
print("The mole fraction of CH4 :", (moleCh4 / sum))
print("The mole fraction of C2H6 : ", (moleC2h6 / sum))
print("The mole fraction of H2 : ", (moleH2 / sum))

print()
print("Concentration of Each Component : ")
print("Concentration of CH4 is : ", moleCh4 / 1000000)
print("Concentration of C2H6 is : ", moleC2h6 / 1000000)
print("Concentration of H2 is : ", moleH2 / 1000000)

print()
print("Partial Pressure of Each Component :")
print("Partial pressure of CH4 is : ", partial(moleCh4),"mmHg")
print("Partial pressure of C2H6 is : ",partial(moleC2h6),"mmHg")
print("Partial pressure of H2 is : ", partial(moleH2),"mmHg")

print()
print("Molar Density of each component :")
print("Molar Density of CH4: ", round((moleCh4/(Ch4*vol/100)),3))
print("Molar Density of C2H6: ", round((moleC2h6/(C2h6*vol/100)),3))
print("Molar Density of H2: ", round((moleH2/(H2*vol/100)),3))

print()
print("Mass Flow Rate of the Mixture is :",flow(moleCh4,moleC2h6,moleH2),"kg/s")

print()
print("Average molecular weight of the mixture : ",flow(moleCh4,moleC2h6,moleH2)*1000/sum," gm")
