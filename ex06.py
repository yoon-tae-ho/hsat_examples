# https://softeer.ai/practice/7626
# 연탄 배달의 시작

import sys

def main():
  
  n = int(input())
  
  answer = 0
  min_dist = 1000001
  
  positions = input().split(" ")

  for i in range(n - 1):
    dist = int(positions[i + 1]) - int(positions[i])
    
    if min_dist > dist:
      min_dist = dist
      answer = 1
    elif min_dist == dist:
      answer += 1
  
  print(answer)

main()