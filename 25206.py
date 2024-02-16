count = 20

time_value = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
score_value = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F', 'P']

total_time = 0
total_score = 0

for _ in range(count):
    title, time, score = input().split()
    time = float(time)

    if score != 'P':
        total_time += time
        total_score += time * time_value[score_value.index(score)]

result = total_score/total_time

print('%.6f' % result)