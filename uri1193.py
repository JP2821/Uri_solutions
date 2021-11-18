casos = int(input())

for i in range(casos):
  A, B = list(map(str,input().split()))
  if B == 'bin':
    C = int(A,2)
    D = format(C, 'x')
    print(f"Case {i+1}:")
    print(f'{C} dec')
    print(f'{D} hex')
    print()
  
  if B == 'dec':
    A = int(A)
    C = format(A, 'b')
    D = format(A, 'x')
    print(f"Case {i+1}:")
    print(f'{D} hex')
    print(f'{C} bin')
    print()
  
  if B == 'hex':
    C = int(A,16)
    D = format(C, 'b')
    print(f"Case {i+1}:")
    print(f'{C} dec')
    print(f'{D} bin')
    print()
