# 配列[True::2]
# → 先頭から2つ目の要素から始まり、2個飛ばし

# 配列[False::3]
# → 先頭から1つ目の要素から始まり、3個飛ばし
print("YNeos"[False::3])

# S が何日連続していたかを算出する
print(len(max("RSR".replace("S", " ").split(" "), key=len)))

# print の中の if文
# 辞書順にしたときに最初の文字を出力
a = "kona"
b = "mai"
print(a if a < b else b)

# 文字列でmax 辞書順
print(max("aaa", "aa"))