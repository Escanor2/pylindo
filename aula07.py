nome = input('Qual é seu nome neném? ')
print('Poxa {:^20} nome de gente legal !'.format(nome))
print('Poxa {:>20} nome de gente legal !'.format(nome))
print('Poxa {:<20} nome de gente legal !'.format(nome))
print('Poxa {:=^20} nome de gente legal !'.format(nome))
print('Poxa {:w^20} nome de gente legal !'.format(nome))
print('Poxa {:1>20} nome de gente legal !'.format(nome))

n1 = int(input("Número"))
n2 = int(input("Número"))
s  = n1+n2
m  = n1*n2
d  = n1/n2
di = n1//n2
e  = n1**n2
print('Entre {} e {} soma {} / multiplicação {} / divisão {:.2f} / \n'
      'divisão inteira {} / potência {}'.format(n1, n2, s, m, d, di, e))