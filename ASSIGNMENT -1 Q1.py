import numpy as np

amount=int(input("Enter the amount of desired mixed acid in Kg : "))

# Coefficients of the equations
A = np.array([
    [1, 1, 1],
    [0.33, 0.95, 0],
    [0.36, 0, 0.78]
])

# Right-hand side of the equations
B = np.array([
    amount,
    0.4*amount,
    0.43*amount
])


answer = np.linalg.solve(A, B) #Solves the equation by taking the coefficient matrix and constant matrix as parameters.
                               # It is a function under numpy lib to solve linear algebra

# Output the results
mixedacid = answer[0]
sulfuricAcid = answer[1]
nitricAcid = answer[2]

print("Required Mass of spent acid: ",round(mixedacid,3), " kg")
print("Required Mass of concentrated sulfuric acid: " ,round(sulfuricAcid,3), " kg")
print("Required Mass of concentrated nitric acid: " ,round(nitricAcid ,3) , "kg")
