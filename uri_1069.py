casos = int(input())

for _ in range(casos):
  string = str(input())
  tamanho = len(string)

  cnt_right = 0
  total = 0

  for i in range(tamanho):
    if string[i] == '<':
      cnt_right += 1
    
    elif string[i] == '>' and cnt_right > 0:
      total += 1
      cnt_right -= 1
  
  print(total)
