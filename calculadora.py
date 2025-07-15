#CALCULADORA BASICA

while True:
  print('Digite a operaçao desejada')
  print('*****************************************')
  print('1-soma')
  print('2-subtração')
  print('3-multiplicação')
  print('4-Divisão')
  print('*****************************************')
  operaçao = input('Digite a opeção desejada')
  numero1_str=input('Digite o primeiro numero:')
  numero2_str= input('Digite o segundo numero:')
  if operaçao.strip() and numero1_str.isdigit() and numero2_str.isdigit():
    numero1 = int(numero1_str)
    numero2= int(numero2_str)

    if operaçao == '1':
      soma = numero1 + numero2
      print(f'O resultado e:{soma}')
    elif operaçao == '2':
      subtraçao = numero1 - numero2
      print(f'O resultado e:{subtraçao}')
    elif operaçao == '3':
      multiplicaçao = numero1 * numero2
      print(f'O resultado e:{multiplicaçao:.0f}')
    elif operaçao == '4':
      divisao = numero1 / numero2
      print(f'O resultado e:{divisao:.0f}')
    outraOperação = input('Deseja fazer outra operação?S(sim) e N(nao)').strip() .upper()
    if outraOperação != 'S':
      break
  else:
    print('Digito invalido')
    
