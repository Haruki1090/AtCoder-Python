"""
問題：連続する部分配列の最大和

問題文
整数が含まれる配列 nums が与えられます。この配列の連続する部分配列を選んだときの、その和の最大値を求めてください。

制約
1 <= numsの長さ <= 10^5
-10^4 <= nums[i] <= 10^4

入力
入力は以下の形式で標準入力から与えられます。
numsの長さ
nums[0] nums[1] ... nums[n-1]

出力
選んだ連続する部分配列の和の最大値を出力してください。

入力例 1
9
-2 1 -3 4 -1 2 1 -5 4

出力例 1
6

解説
入力例 1 の場合、[4, -1, 2, 1] が連続する部分配列の和として最大となるため、その和の 6 を出力します。
"""

n_range = int(input())
nums = list(map(int, input().split()))

count = 0
pre_cpunt = 0

i = 0
j = 1

for i in range(n_range + 1):
    for j in range(n_range + 1):
        pre_cpunt = sum(nums[i:j])
        if count < pre_cpunt:
            count = pre_cpunt

print(count)

