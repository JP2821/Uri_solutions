def porcentagem(lista):
  media = 0 
  contador =0
  tamanho = len(lista)
  for i in range(tamanho):
    media = media + int(lista[i]) 

  media = media/tamanho

  for i in range(tamanho):
    if int(lista[i]) > media:
      contador += 1

  print(f'{(contador/tamanho)*100:.3f}%')

entrada = int(input()) 

for _ in range(entrada):
  lista_entrada = input().split()
  lista_entrada.remove(lista_entrada[0])
  porcentagem(lista_entrada)
