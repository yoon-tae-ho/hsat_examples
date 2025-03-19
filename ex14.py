# https://softeer.ai/practice/9498
# [한양대 HCPC 2023] Yeah, but How?

def main():
  s = input().strip()
  answer = ""
  
  for c in s:
    if c == "(":
      answer += "("
    else:
      answer += "1)+"
  
  print(answer[:-1])

main()