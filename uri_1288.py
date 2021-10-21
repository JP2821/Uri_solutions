def knapsack(carga_da_mochila,lista_peso,lista_poder, tipos_de_bala):
  if tipos_de_bala == 0 or carga_da_mochila == 0:
    return 0
  
  if lista_peso[tipos_de_bala - 1] > carga_da_mochila:
    return knapsack(carga_da_mochila, lista_peso, lista_poder,tipos_de_bala - 1)
  
  else:
    return max(lista_poder[tipos_de_bala-1] + knapsack(carga_da_mochila - lista_peso[tipos_de_bala-1], lista_peso, lista_poder,tipos_de_bala - 1), knapsack(carga_da_mochila, lista_peso, lista_poder,tipos_de_bala - 1))

casos = int(input())
lista_poder = []
lista_peso = []

for i in range(casos):
  tipos_de_bala = int(input())
  
  for j in range(tipos_de_bala):
    poder,peso = input().split()
    
    poder = int(poder)
    lista_poder.append(poder)
    
    peso = int(peso)
    lista_peso.append(peso)

  carga_da_mochila = int(input())
  vida_do_muro = int(input())

  resultado = knapsack(carga_da_mochila,lista_peso,lista_poder, tipos_de_bala)

  lista_poder.clear()
  lista_peso.clear()

  if resultado >= vida_do_muro:
    print("Missao completada com sucesso")
  
  else:
    print("Falha na missao")
