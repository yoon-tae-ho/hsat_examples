# https://softeer.ai/practice/7353
# 나무 심기

def main():
  n = int(input())
  F_list = list(map(int, input().strip().split(" ")))
  
  F_list.sort()
  
  max = F_list[0] * F_list[1]
  min = F_list[-1] * F_list[-2]
  
  print(max if max > min else min)

main()