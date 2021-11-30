while 1:
  entrada = int(input())
  lista = []

  if entrada == 0:
    break 

  else:
    for i in range(entrada):
      lista.append(i+1)

    tamanho = len(lista)
    lista_aux = []

    while (tamanho != 1):
      lista_aux.append(lista[0])
      lista.append(lista[1])
      lista.pop(0)
      lista.pop(0)
      tamanho = len(lista)

    print("Discarded cards: ", end = '')
    print(", ".join( repr(e) for e in lista_aux ))
    print("Remaining card: ", end = '')
    print("".join( repr(e) for e in lista ))
