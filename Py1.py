import math
n = float(input('Digite um número '))
n1 = int(input('Digite um número '))


print("A raiz quadrada de {} é {:.2f}".format(n,math.sqrt(n)))
print("A redondado pra cima de é {}".format(n,math.ceil(n)))
print("Os valores {} e {} são proximos? {}"
.format(n,n1,(math.isclose(n, n1, rel_tol=0.05, abs_tol=0.0))))


