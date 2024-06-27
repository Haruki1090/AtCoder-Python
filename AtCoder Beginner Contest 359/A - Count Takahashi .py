N = int(input())
lines = [input() for _ in range(N)]

index = 0

for line in range (0, N):
    if lines[line] == "Takahashi":
        index = index + 1

print(index)