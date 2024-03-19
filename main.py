print('Bem vindo a sorveteria da Francielli Fagundes de Souza!')
print(35*'-'+'Cardápio'+36*'-')
print('Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)')
print('     1      |        R$ 6,00         |      R$ 7,00       |       R$ 8,00      ')
print('     2      |        R$ 11,00        |      R$ 13,00      |       R$ 15,00     ')
print('     3      |        R$ 15,00        |      R$ 18,00      |       R$ 21,00     ')
print(79*'-')
acumulador=0
while True:
  sabor = input('Digite o sabor desejado (tr/es/pr):')
  if sabor != 'tr' and sabor != 'es' and sabor != 'pr':
    print('Opção inválida!. Tente novamente')
    continue #se o usuário digitar algo errado, irá recomeçar o while
  bolas = input('Digite a quantidade de bolas desejadas (1/2/3):')

  if bolas != '1' and bolas != '2' and bolas != '3':
    print('Opção inválida!. Tente novamente')
    continue #se o usuário digitar algo errado, irá recomeçar o while

  if sabor=='tr' and bolas=='1':
    print(' Você escolheu 1 bola de sorvete no sabor Tradicional: R$ 6,00')
    acumulador=acumulador + 6 #Pegar o valor que tinha no acumulador e somar com 6

  elif sabor=='tr' and bolas=='2':
    print(' Você escolheu 2 bolas de sorvete no sabor Tradicional: R$ 11,00')
    acumulador=acumulador + 11 #Pegar o valor que tinha no acumulador e somar com 11

  elif sabor=='tr' and bolas=='3':
    print(' Você escolheu 3 bolas de sorvete no sabor Tradicional: R$ 15,00')
    acumulador=acumulador + 15 #Pegar o valor que tinha no acumulador e somar com 15

  elif sabor=='pr' and bolas=='1':
    print(' Você escolheu 1 bola de sorvete no sabor Premium: R$ 7,00')
    acumulador=acumulador + 7 #Pegar o valor que tinha no acumulador e somar com 7

  elif sabor=='pr' and bolas=='2':
    print(' Você escolheu 2 bolas de sorvete no sabor Premium: R$ 13,00')
    acumulador=acumulador + 13 #Pegar o valor que tinha no acumulador e somar com 13

  elif sabor=='pr' and bolas=='3':
    print(' Você escolheu 3 bolas de sorvete no sabor Premium: R$ 18,00')
    acumulador=acumulador + 18 #Pegar o valor que tinha no acumulador e somar com 18

  elif sabor=='es' and bolas=='1':
    print(' Você escolheu 1 bola de sorvete no sabor Especial: R$ 8,00')
    acumulador=acumulador + 8 #Pegar o valor que tinha no acumulador e somar com 8

  elif sabor=='es' and bolas=='2':
    print(' Você escolheu 2 bolas de sorvete no sabor Especial: R$ 15,00')
    acumulador=acumulador + 15 #Pegar o valor que tinha no acumulador e somar com 15

  elif sabor=='es' and bolas=='3':
    print(' Você escolheu 3 bolas de sorvete no sabor Especial: R$ 21,00')
    acumulador=acumulador + 21 #Pegar o valor que tinha no acumulador e somar com 21

  mais_pedido=input('Deseja mais algum sorvete (S/N)?')
  mais_pedido=mais_pedido.upper() #Resolução para o problema de digitação 's' e 'S' ou 'n' e 'N'
  if mais_pedido == 'S':
    continue
  else:
    print('O valor total a ser pago é de: R${:.2f}'.format(acumulador))
    break
