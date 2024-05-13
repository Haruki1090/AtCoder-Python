# 10 以下の適当な正の数の組を 5 個入れたリストを用意し，任意の 10 以下の正の整数をキーボードから受け取って，その数がリストに入っているか否かを判定するプログラムを書きなさい．

import random

numbers_list = []

for n in range(5):
    numbers_list.append(random.randint(1,10))
    # print(numbers_list) # appendのテスト

what_is_the_number = int(input("1から10までの数字を入力してください: "))

print("生成されたリスト: ", numbers_list)

if what_is_the_number in numbers_list:
    print("数", what_is_the_number, "はリスト内に存在します")
else:
    print("数", what_is_the_number, "はリスト内に存在しません")