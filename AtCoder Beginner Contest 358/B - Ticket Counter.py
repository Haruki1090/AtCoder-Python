n, a = map(int, input().split())
t = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        time = t[i] + a
        print(time)
    elif t[i] < time:
        time = time + a
        print(time)
    else:
        time = t[i] + a
        print(time)
