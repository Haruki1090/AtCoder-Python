# 辺の長さを指定することで「正三角形の面積」「正三角柱の体積」「正三角柱の表面積」を計算する関数を作成し，すべて実行しなさい．（他の人と異なるプログラムを評価します）
# ヒント：[mathライブラリ](http://docs.python.jp/3/library/math.html)にある三角関数や平方根の関数を利用すると良い．

import math

def triangle_area(side):
    return (math.sqrt(3) / 4) * (side ** 2)

def prism_volume(side, height):
    base_area = triangle_area(side)
    return base_area * height

def prism_surface_area(side, height):
    base_area = triangle_area(side)
    lateral_area = 3 * side * height
    return 2 * base_area + lateral_area

side = int(input("正三角形の一辺の長さを入力してください: "))
height = int(input("正三角柱の高さを入力してください: "))

area = triangle_area(side)
volume = prism_volume(side, height)
surface_area = prism_surface_area(side, height)

print("正三角形の面積: {:.1f}".format(area))
print("正三角柱の体積: {:.1f}".format(volume))
print("正三角柱の表面積: {:.1f}".format(surface_area))