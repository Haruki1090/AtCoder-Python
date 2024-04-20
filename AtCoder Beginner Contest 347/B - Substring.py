# 問題文
# 英小文字からなる文字列 S が与えられます。
# S の空でない部分文字列は何種類ありますか？
# ただし、部分文字列とは連続する部分列のことを指します。例えば、xxx は yxxxy の部分文字列ですが、xxyxx の部分文字列ではありません。

S = input()

def count_unique_substrings(S):
    unique_substrings = set()
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            unique_substrings.add(S[i:j])
    return len(unique_substrings)

print(count_unique_substrings(S))