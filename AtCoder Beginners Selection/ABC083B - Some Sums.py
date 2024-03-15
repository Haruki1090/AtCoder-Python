# 問題文
# 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

# 制約
# 1≤N≤10^4
# 1≤A≤B≤36
# 入力はすべて整数である

# 入力
# 入力は以下の形式で標準入力から与えられる。
# N A B

# 出力
# 1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を出力せよ。

n, a, b = map(int, input().split())

def sum_of_digits(n):
    s = str(n) # Stringで受け取る。Strで受け取ると一文字ずつ分解できる。
    array = list(map(int, s)) # それぞれの文字をintに変換してリストにする。
    return sum(array) # リスト要素の合計を返す。

count = 0;

for i in range(1, n+1):
    if a <= sum_of_digits(i) <= b:
        count += i
print(count);