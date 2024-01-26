sum = int(input())
count = int(input())

num = 0
i = 0

for i in range(count):
    a, b = map(int, input().split())
    num += a * b
    if i == count:
        break

if(sum == num):
    print("Yes")
else:
    print("No")