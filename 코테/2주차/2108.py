from collections import Counter
import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

mean = round(sum(numbers) / N)

numbers.sort()
median = numbers[N//2]

count = Counter(numbers)
max_freq = max(count.values())
modes = []
for num in count:
    if count[num] == max_freq:
        modes.append(num)
modes.sort()  
mode = modes[1] if len(modes) > 1 else modes[0]

range_value = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_value)
