# 再帰を用いて「最大公約数」「最大公倍数」を計算する関数を作成し，実行しなさい．（ただし，mathライブラリに用意されている最大公約数の関数 `math.gcd()` など，ライブラリで提供されている機能は使わないこと）

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = int(input("最大公約数と最小公倍数を求める2つの整数を入力してください (1つ目): "))
num2 = int(input("最大公約数と最小公倍数を求める2つの整数を入力してください (2つ目): "))

greatest_common_divisor = gcd(num1, num2)
least_common_multiple = lcm(num1, num2)

print("最大公約数 (GCD):", greatest_common_divisor)
print("最小公倍数 (LCM):", least_common_multiple)
