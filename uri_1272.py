def decodificando(palavra):
  tamanho = len(palavra)
  nova_palavra = ""
  for i in range(0,(tamanho-1)):
    if i == 0 and palavra[0] != " ":
      nova_palavra = nova_palavra + palavra[0]
    if palavra[i] == " " and palavra[i+1] != " ":
      nova_palavra = nova_palavra + palavra[i+1]

  return nova_palavra
      

entrada = int(input())

for i in range(0,entrada):
  palavra = str(input())
  resultado = decodificando(palavra)
  print(resultado)
  
