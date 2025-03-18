# https://softeer.ai/practice/6254
# 근무 시간

def main():
  
  answer = 0
  
  for i in range(5):
    times = input().strip().split(" ")
    time_1 = list(map(int, times[0].split(":")))
    time_2 = list(map(int, times[1].split(":")))

    delta_h = time_2[0] - time_1[0]
    delta_m = time_2[1] - time_1[1]
    
    answer += 60 * (delta_h if delta_m > 0 else delta_h - 1)
    
    answer += delta_m if delta_m > 0 else 60 + delta_m
    
  print(answer)

main()