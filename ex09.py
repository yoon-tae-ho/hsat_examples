# https://softeer.ai/practice/6295
# A+B

def main():
  
  T = int(input())
  
  for i in range(T):
    [A, B] = list(map(int, input().strip().split(" ")))
    
    print(f"Case #{i + 1}: {A + B}")

main()