casos = int(input())
lista = list()
cnt = 0
cnt_exclusao = 0

for i in range(casos):
  pokemon = str(input())
  lista.append(pokemon)

nova_lista = set(lista) #usamos a função set para excluir elementos repetidos

tamanho = len(nova_lista)

resultado = 151 - tamanho

print(f'Falta(m) {resultado} pomekon(s).')
