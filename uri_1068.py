while 1:
  try:
    entrada = str(input())
    cnt = 0
    cnt_aux = 0
    tamanho = len(entrada)
    for i in range(tamanho):
      if entrada[i] == '(':
        cnt += 1
      
      if entrada[i] == ')':
        cnt -=1

      if cnt < 0:
        break  

    if cnt == 0:
      print("correct")
    else:
      print("incorrect")

  except EOFError:
    break
