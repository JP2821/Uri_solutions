#{ n*(n+1)*(2n+1) }/6 

def feyman(num):
  soma = (num * (num+1)*(2*num+1))
  resultado = int(soma/6)
  
  print(resultado)

while 1:
  numero = int(input())
  if numero == 0:
    break
  else:
    feyman(numero)
