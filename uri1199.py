while 1:
  numero = str(input())

  if numero == "-1":
    break
  else:
    if numero[0] == "0" and numero[1] == 'x':
      numero = int(numero,16)
      print(numero)
    else:
      numero = int(numero)
      numero = hex(numero)
      numero = numero[:2] + numero[2:].upper()
      print(numero)
