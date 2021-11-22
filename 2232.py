#{ (2^n)-1 }

def triangulo_de_pascal(num):
  soma = (2**num) - 1
  print(soma)

casos = int(input())

for _ in (range(casos)):
  numero = int(input())
  triangulo_de_pascal(numero)
