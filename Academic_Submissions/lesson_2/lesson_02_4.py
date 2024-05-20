x = 25 # 与える整数
epsilon = 0.1 # ほぼ同じ値とみなす範囲
step = epsilon**2 # 刻み幅の設定
repCount = 0
ans = 0.0 # 近似的な平方根を表す数
print(ans, x)
while abs(ans**2 - x) >= epsilon and ans**2 <= x: # stepの刻み幅で大きくなる数ansの２乗と与えた整数の差の絶対値がepsilonの範囲以上，かつansが与えた整数以下という条件
    ans += step  # stepの刻み幅だけ大きくする
    repCount+= 1 # カウンタ変数を1増やす
    #print(ans)
print("repCount =", repCount) # 繰り返し回数の表示
if  abs(ans**2 - x) >= epsilon: # ansの２乗と与えた整数の差の絶対値がepsilonの範囲以上という条件
    print(x, "の平方根（近似値）を作れませんでした．")
else:                          # ansの２乗と与えた整数の差の絶対値がepsilonの範囲未満という条件
    print(ans, "は", x, "の平方根にとても近いです．")