entrada = input().split(" ")
acumulador_crescente = 0
acumulador_decrescente = 0
lista = []
tamanho = len(entrada)

for i in range(0,(tamanho)):
  lista.append(int(entrada[i]))

for i in range(0,(tamanho-1)):
  if lista[i] > lista[i+1]:
    acumulador_decrescente += 1
  elif lista[i] < lista[i+1]:
    acumulador_crescente += 1



if acumulador_decrescente == (tamanho-1):
  print('D')
elif acumulador_crescente == (tamanho-1):
  print('C')
else :
  print('N')
