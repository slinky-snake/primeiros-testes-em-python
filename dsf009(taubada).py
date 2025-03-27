print('olá, bom dia, me diga um número e direi sua tabuada!\n>>>')
ah=int(input('diga o número '))

for i in range(0,21):
  soma = ah * i
  print(f'{i} x {ah}={soma}')
