"""
問題：文字列の圧縮

問題文
文字列 S が与えられます。この文字列に含まれる連続する文字を、その文字とその文字が連続する数によって圧縮した新しい文字列を出力してください。例えば、'aaaabcccaa' を圧縮すると 'a4b1c3a2' となります。

制約
1 <= Sの長さ <= 10^4
S は英小文字のみから構成される

入力
入力は以下の形式で標準入力から与えられます。
S

出力
文字列 S を圧縮した結果を出力してください。

入力例 1
aaaabcccaa

出力例 1
a4b1c3a2

入力例 2
abc

出力例 2
a1b1c1

解説
入力例 1 の場合、'a' が4回、'b' が1回、'c' が3回、再び 'a' が2回連続しているため、'a4b1c3a2' という圧縮結果が得られます。
入力例 2 の場合、どの文字も連続していないため、各文字をそのまま '1' 回と数えて 'a1b1c1' と出力します。
"""

# s = input()
# count = 1

# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count += 1
#     else:
#         print(s[i-1] + str(count))
#         count = 1
# print(s[-1] + str(count))

# レビュー
# 大体合ってるが、出力形式が違う。

# 改善コード
s = input()
compressed = ""  # 圧縮結果を格納する文字列を初期化
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        compressed += s[i-1] + str(count)  # 圧縮結果に追加
        count = 1 # カウントをリセット

compressed += s[-1] + str(count)  # 最後の文字とその数を追加。 -1は最後の文字のこと。ちなみに-2は最後から2番目の文字のこと。
print(compressed)