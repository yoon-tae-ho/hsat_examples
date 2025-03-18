# https://softeer.ai/practice/6253
# 주행거리 비교하기

def main():
  
  [A, B] = list(map(int, input().strip().split(" ")))
  
  if A > B:
    print("A")
  elif A < B:
    print("B")
  else:
    print("same")

main()