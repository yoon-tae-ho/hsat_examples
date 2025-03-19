# https://softeer.ai/practice/9657
# 나무 공격

def main():
  
  [n, m] = list(map(int, input().strip().split(" ")))
  
  field = []
  
  for i in range(n):
    field.append(list(map(int, input().strip().split(" "))))
  
  [L1, R1] = list(map(int, input().strip().split(" ")))
  [L2, R2] = list(map(int, input().strip().split(" ")))
  
  for i in range(L1 - 1, R1):
    if 1 in field[i]:
      field[i][field[i].index(1)] = 0
  
  for i in range(L2 - 1, R2):
    if 1 in field[i]:
      field[i][field[i].index(1)] = 0
  
  count = 0
  for i in range(n):
    for j in range(m):
      if field[i][j] == 1:
        count += 1
        
  print(count)


main()