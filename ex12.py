# https://softeer.ai/practice/11001
# GPT식 숫자 비교

def compare(a, b):
  if a.find(".") != -1:
    a = a.split(".")
    ax = int(a[0])
    ay = int(a[1])
  else:
    ax = int(a)
    ay = -1
  
  if b.find(".") != -1:
    b = b.split(".")
    bx = int(b[0])
    by = int(b[1])
  else:
    bx = int(b)
    by = -1
  
  if ax != bx:
    return ax > bx
  else:
    return ay > by

def main():
  
  N = int(input())
  
  numbers = []
  
  for i in range(N):
    numbers.append(input().strip())
  
  for i in range(N - 1):
    for j in range(i + 1, N):
      if compare(numbers[i], numbers[j]):
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp
  
  for i in range(N):
    print(numbers[i])

main()