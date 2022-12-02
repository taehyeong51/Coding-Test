N = int(input())

heights = [int(input()) for _ in range(N)]
inv_heights = list(reversed(heights))

max_height = heights[0]
inv_max_height = inv_heights[0]

cnt = 1
inv_cnt = 1

for idx,(height,inv_height) in enumerate(zip(heights,inv_heights)):
    if idx == 0:
        continue
    if height > max_height:
        max_height = height
        cnt += 1
      
    if inv_height > inv_max_height:
        inv_max_height = inv_height
        inv_cnt += 1


print(cnt)
print(inv_cnt)