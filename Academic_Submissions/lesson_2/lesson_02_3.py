x = int(input("任意の整数を入力してください？"))
for cube_root in range(abs(x)): # 0から与えた整数の絶対値までくり返すループ
    if cube_root**3 >= abs(x): # 0から与えられた整数xの絶対値まで順にカウンタ変数cube_rootを３乗し，xの絶対値以上の場合ループを抜ける
        break
if cube_root**3 != abs(x): # ループを抜けたときにおいて，cube_rootの３乗がxの絶対値の３乗に等しくない場合
    print(x, "は完全立方ではありません．")
else:                      # ループを抜けたときにおいて，cube_rootの３乗がxの３乗に等しい場合
    if x < 0:              # xが負の場合
         cube_root = cube_root*(-1) #cube_rootを負にする
    print(x, "の完全立方は", cube_root)