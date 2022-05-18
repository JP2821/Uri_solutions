def fatorial(numero):
  if numero == 0 or numero == 1:
    return 1
  else:
    return numero * fatorial(numero - 1)

while True:
  acumulador = 0
  numero = str(input())
  if numero == "0":
    break

  tamanho = len(numero)
  i=0
  while tamanho != 0:
    resultado = fatorial(int(tamanho))
    acumulador = acumulador + (int(numero[i]) * resultado)
    tamanho = tamanho - 1
    i+=1
  print(acumulador)
