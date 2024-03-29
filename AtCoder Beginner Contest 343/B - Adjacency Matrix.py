# 問題文
# N 頂点の単純無向グラフ G があり、グラフの頂点には 1,2,…,N の番号が付けられています。
# G の隣接行列 (A_i,j) が与えられます。
# すなわち、
# G は A_i,j=1 であるとき、またそのときに限り頂点 i と頂点 j を結ぶ辺を持ちます。
# i=1,2,…,N について、頂点 i と直接結ばれている頂点の番号を昇順に出力してください。
# ただし、頂点 i と頂点 j が直接結ばれているとは、頂点 i と頂点 j を結ぶ辺が存在することをいいます。

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # 2次元配列を作成
for i in range(n):
    l = [j+1 for j in range(n) if a[i][j] == 1] # 1の位置のインデックスに1を足して出力
    print(*l) # これは、隣接行列の各行を見て、1の位置のインデックスに1を足して出力している。