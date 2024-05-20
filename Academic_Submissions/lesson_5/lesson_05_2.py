# CP_04data.txt は，青空文庫 (※) からダウンロードした「吾輩は猫である」[https://www.aozora.gr.jp/cards/000148/card789.html] の本文部分である．この文章の中に猫という文字は何個あるか? CP_04data.txt を読み込み，次の2つの方法で「猫」の数を数えて出力するプログラムを作成しなさい．

# 1. 文字列型の count() メソッドを使用した方法．
# 2. 文字列型の count() メソッドを使用せずに数える方法．(他の人と異なるプログラムを評価します) 

# 2つの方法を実行する単一のプログラムを提出すること．


opend_file = open("CP_04data.txt", "r", encoding="shift-jis") # エンコードはshift-jisを指定
scaned_text = opend_file.read()

# 方法1: Count()を利用し、猫の出現回数をカウントする方法
sum_by_count = scaned_text.count("猫") 

# 方法2: List変換しfilter()を利用することで、猫の出現回数をカウントする方法
converted_list = list(scaned_text) # 変換
filtered_list = list(filter(lambda char: char == '猫', converted_list)) #filter()により猫のみを抽出する

print("猫の出現回数(Count()の結果): ", sum_by_count) # 方法1の出力
print("猫の出現回数(filter()の結果): ", len(filtered_list)) # 方法2の出力