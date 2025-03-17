# https://softeer.ai/practice/7368
# 위험한 효도

def main():
  [a, b, d] = list(map(int, input().split(" ")))
  
  answer = 0
  
  answer += (d // a) * (a + b)
  
  if d % a == 0:
    answer -= b
  answer += d % a
  
  answer += (d // b) * (a + b)
  
  if d % b == 0:
    answer -= a
  answer += d % b
  
  print(answer)

main()