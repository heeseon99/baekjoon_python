num = [i for i in range(1, 31)]

for _ in range(28):
    check = int(input())
    num.remove(check)

print(num[0])
print(num[1])