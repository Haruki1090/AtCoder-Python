# レポート課題6-1で作成した3つの関数を，モジュールファイル（".py" で終わる名前のファイル）の中にまとめなさい．そのうえで，作成したモジュールファイルを import 文によりモジュールとして読み込んで，モジュール内の関数をすべて実行しなさい．

import geometry_utils as gu

side_length = int(input("正三角形の一辺の長さを入力してください: "))
height = int(input("正三角柱の高さを入力してください: "))

triangle_area = gu.triangle_area(side_length)
print("正三角形の面積: {:.3f}".format(triangle_area))

prism_volume = gu.prism_volume(side_length, height)
print("正三角柱の体積: {:.3f}".format(prism_volume))

prism_surface_area = gu.prism_surface_area(side_length, height)
print("正三角柱の表面積: {:.3f}".format(prism_surface_area))