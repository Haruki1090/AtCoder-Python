# 問題文
# 髙橋君はサッカーの試合で N 回ペナルティキックを蹴ります。
# 髙橋君は i 回目のペナルティキックでは、 i が 3 の倍数の場合は失敗しそれ以外の場合は成功します。
# 髙橋君がペナルティキックを蹴ったときの結果を出力してください。

# ooxooxo と出力されれば良い

n = int(input())
ans = ""
for i in range(n):
    if (i+1) % 3 == 0:
        ans += "x"
    else:
        ans += "o"
print(ans)