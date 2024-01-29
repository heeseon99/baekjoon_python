n = int(input())
num = map(int, input().split())
search = int(input())
count = 0

for i in num:
    if i == search:
        count += 1

print(count)
