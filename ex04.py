# https://softeer.ai/practice/7698
# [한양대 HCPC 2023] 개표

import sys

def main():
  T = int(input())
  
  for i in range(T):
    n = int(input())
    
    while (n // 5) > 0:
      print("++++", end=" ")
      n -= 5
    
    while n > 0:
      print("|", end="")
      n -= 1
    
    print()

main()