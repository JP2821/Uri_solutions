casos = int(input())
cnt = 0
one = 'one'
two = 'two'
three = 'three'

for i in range(casos):
  cnt=0
  palavra = str(input())
  tamanho = len(palavra)

  if tamanho == 3:
      if palavra[0] == 'o':
        cnt += 1
      if palavra[1] == 'n':
        cnt += 1
      if palavra[2] == 'e':
        cnt += 1
    
      if cnt >= 2:
        print('1')

      else:
        print('2')
      

  else:
    print('3')
