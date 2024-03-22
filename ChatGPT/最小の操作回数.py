"""
問題：最小の操作回数

問題文
整数 N が与えられます。次の操作を用いて、N を 1 にするまでの最小の操作回数を求めてください。
操作:N が偶数の場合、N を 2 で割る。N が奇数の場合、N に 1 を足すか、1 を引く。

制約
1 <= N <= 10^6

入力
入力は以下の形式で標準入力から与えられます。
N

出力
N を 1 にするまでの最小の操作回数を出力してください。

入力例 1
8

出力例 1
3

入力例 2
7

出力例 2
4

解説
入力例 1 の場合、8 -> 4 -> 2 -> 1 と操作を行うことで、3回で 1 にすることができます。
入力例 2 の場合、7 -> 6 -> 3 -> 2 -> 1 または 7 -> 8 -> 4 -> 2 -> 1 のように、4回の操作で 1 にすることができます。
"""

# n = int(input())

# count = 0

# while n != 1:
#     # nが偶数の場合
#     if n % 2 == 0:
#         n = n/2 
#     # nが奇数の場合
#     else:
#         n += 1
#     count += 1

# print(count)


# 改善コード

n = int(input())

count = 0

while n != 1:
    if n % 2 == 0:
        n = n // 2  #整数の割り算の時は//を使う
    else:
        # nに1を足した場合と引いた場合のどちらがより効率的か判断
        # 4の倍数の場合は1を引く方が効率的
        if (n+1) % 4 == 0 and n != 3:
            n += 1
        else:
            n -= 1
    count += 1

print(count)