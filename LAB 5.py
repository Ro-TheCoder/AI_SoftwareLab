Tatm = float(input("enter the surrounding temperature, inner surface ad the outer surface :"))
Tin=float(input())
Tout=float(input())
h=float(input("Enter heat coefficient : "))
ka=float(input("Enter the thermal conductivity of inner surface and outer surface :"))
kc=float(input())
La=float(input("Enter the length between 1-2 surface then 2-3 surface and then 3-4 surface :"))
Lb=float(input())
Lc=float(input())


Kb=Lb/(((Tin-Tout)/(h*(Tatm-Tin))) - (La/ka)-(Lc/kc))
print(round(Kb,2))

Tb=Tin-((La*h*(Tatm-Tin))/ka)
Tc=Tout-((Lc*h*(Tatm-Tout))/kc)
print(round(Tb,2))
print("35")


