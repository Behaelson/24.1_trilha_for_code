import math
n = 2

for n in range(2, 1000000):
    X = float(1/(n*(math.log(n))**2))
    n = n + 1
    print(X)

# O Resultado converge para um número a 10^-9. 
# depende da perspectiva de intervalo de cada um para definir se converge ou não...