import math
import random
import emoji
from math import ceil, floor

n = int(input("Digite um número "))
raiz = math.sqrt(n)
print("A raiz é {:.2f} ".format(raiz))
print("A raiz é {:.2f} ".format(math.floor(raiz)))
print("A raiz é {:.2f} ".format(math.ceil(raiz)))

num = random.randint(1,10)
print(num)

print(emoji.emojize("Meow 👨‍👩🏿‍👧🏻‍👦🏾"))
print(emoji.emojize('Python is :thumbs_up:'))


#print("{}".format(math.ceil(n)))
#print("{}".format(math.floor(n)))
#print("{}".format(math.trunc(n)))
#print("{}".format(math.pow(n)))
#print("{}".format(math.sqrt(n)))
#print("{}".format(math.factorial(n)))