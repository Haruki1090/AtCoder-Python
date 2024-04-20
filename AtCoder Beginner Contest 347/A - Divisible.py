# 問題文
# 正整数 N,K 及び長さ N の数列 A=(A_1,A_2,…,A_N) が与えられます。
# A に含まれる要素のうち、K の倍数であるもののみを全て取り出し、それらを K で割って出力してください。


n,k = map(int, input().split())
a = list(map(int, input().split()))

ans = list()

for i in range(n):
    if a[i] % k == 0:
        ans.append(a[i]//k)
print(*ans)