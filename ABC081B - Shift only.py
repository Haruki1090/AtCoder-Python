# 問題文
# 黒板に N 個の正の整数 A_1 ,...,A_Nが書かれています

# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．

# 黒板に書かれている整数すべてを 2 で割ったものに置き換える．
# すぬけ君は最大で何回操作を行うことができるかを求めてください．

# 制約
# 1 ≤ N ≤ 200
# 1 ≤ A_i ≤ 10^9

N = int(input()) # N個の整数
A = list(map(int, input().split())) # N個の整数をリストに格納

for i in range(N):
    count = 0
    while A[i] % 2 == 0:
        A[i] = A[i] / 2
        count += 1
    if i == 0:
        max_count = count
    elif count < max_count:
        max_count = count
print(max_count)