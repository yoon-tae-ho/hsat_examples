# https://softeer.ai/practice/7695
# [한양대 HCPC 2023] Tren del Fin del Mundo

def main():
  N = int(input())
  
  answer_x = 1001
  answer_y = 1001
  for i in range(N):
    coord = input().split(" ")
    if answer_y > int(coord[1]):
      answer_x = int(coord[0])
      answer_y = int(coord[1])
  
  print(f"{answer_x} {answer_y}")

main()