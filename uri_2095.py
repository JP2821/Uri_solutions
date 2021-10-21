casos = int(input())

cnt = 0

quadradônia = []

quadradônia.append(str(input()))

quadradônia = quadradônia[0].split(" ")

for i in range(casos):
  quadradônia[i] = int(quadradônia[i]) 

quadradônia.sort()

nlogoniano = []

nlogoniano.append(str(input()))

nlogoniano = nlogoniano[0].split(" ")

for i in range(casos):
  nlogoniano[i] = int(nlogoniano[i])

nlogoniano.sort()

for i in range(casos):
  for j in range(casos):
    if nlogoniano[i] > quadradônia[j]:
      cnt+=1
      quadradônia[j] = nlogoniano[casos-1]
      break

print(cnt)
