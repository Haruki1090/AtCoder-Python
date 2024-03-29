"""
問題：配列の要素のシフト

問題文
整数 N と整数 K、そして N 個の整数が含まれる配列 A が与えられます。この配列の要素を K 回だけ右にシフトさせた結果を出力してください。配列の要素は 1-indexed であるとします（つまり、配列の最初の要素は A[1]、最後の要素は A[N] です）。

制約
1 <= N <= 10^5
0 <= K <= 10^9
-10^9 <= A[i] <= 10^9 （すべての i について 1 <= i <= N）

入力
入力は以下の形式で標準入力から与えられます。
N K
A[1] A[2] ... A[N]

出力
配列の要素を K 回右にシフトさせた結果を出力してください。配列の要素は空白で区切ってください。

入力例 1
5 2
1 2 3 4 5

出力例 1
4 5 1 2 3

入力例 2
4 1
-3 0 3 -2

出力例 2
-2 -3 0 3

解説
入力例 1 の場合、配列 [1, 2, 3, 4, 5] を右に2回シフトさせると、[4, 5, 1, 2, 3] となります。
入力例 2 の場合、配列 [-3, 0, 3, -2] を右に1回シフトさせると、[-2, -3, 0, 3] となります。
"""

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# do_shift = k % n # 配列の要素数で割った余りがシフトする回数

# slided_array = a[-do_shift:] + a[:-do_shift]
# print(slided_array)

# 改善コード
n, k = map(int, input().split())
a = list(map(int, input().split()))

do_shift = k % n  # 配列の要素数で割った余りがシフトする回数

slided_array = a[-do_shift:] + a[:-do_shift]
print(' '.join(map(str, slided_array)))  # 空白で要素を区切って出力
