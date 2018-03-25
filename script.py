# coding:utf-8

# 変数nに「ねこ」を代入してください
n = "ねこ"

# 変数nを出力してください
print (n)

#「n」という文字列を出力してください
print ("n")

# 変数nに3 + 7を代入してください
n = 3 + 7

# 変数nを出力してください
print (n)

m = "ねこ"
print (m)

# 変数mに「いぬ」を上書きして、出力してください
m = "いぬ"

print (m)


n = 14
print(n)

# 変数nに5をかけて上書きしてください
n = n * 5

print(n)

# 変数に「東京」を代入してください
p = "東京"

# 変数pを用いて「私は東京出身です」と出力してください
print("私は" + p + "出身です")

h = 1.7
w = 60

# 変数h,wの型を出力してください
print(type(h))
print(type(w))

# 変数bmiに計算結果を代入してください
bmi = w / h ** 2

# 変数bmiを出力してください
print(bmi)

# 変数bmiの型を出力してください
print(type(bmi))

# 「あなたのbmiは○○です」と出力してください
print("あなたのbmiは" + str(bmi) + "です")

# 4 + 6と-10を「!=」を用いて関係式を作り出力してください。
print (4 + 6 != -10)

n = 14

# ifを用いて変数nが15より大きい場合「とても大きい数字。」と出力してください
if n >= 15:
    print("とても大きい数字。")
elif n >= 11:
    print("中くらいの数字。")
else:
    print("小さい数字。")

n_1 = 14
n_2 = 28

# n_1が8より大きく14より小さい条件式を作りandを用いて出力してください
print(n_1 > 8 and n_1 < 14)

# n_1の2乗がn_2の5倍より小さい条件式を作りnotを用いて出力してください
print(not(n_1 ** 2 < n_2 * 5))


# 変数colorに「red」「blue」「yellow」の3つの文字列を代入してください。
color = ["red", "blue", "yellow"]

print(color)

# colorの型の出力
print(type(color))

apple = 4
grape = 3
banana = 6

# 変数名fruitsにリスト型で変数を要素としてapple、grape、bananaの順に格納してください
fruits = [apple, grape, banana]

print(fruits)

fruits_name_1 = 'りんご'
fruits_num_1 = 2
fruits_name_2 = 'みかん'
fruits_num_2 = 10

# [["りんご", 2], ["みかん", 10]]という出力になるように、fruitsに変数をリスト型に代入してください
fruits = [[fruits_name_1, fruits_num_1], [fruits_name_2, fruits_num_2]]

# 出力
print(fruits)


fruits = ["apple", 2, "orange", 4, "grape", 3, "banana", 1]

# 変数fruitsの2番目の要素を出力してください
print(fruits[1])

# 変数fruitsの最後の要素を出力してください
print(fruits[-1])


chaos = ["cat", "apple", 2, "orange", 4, "grape", 3, "banana", 1, "elephant", "dog"]

# 変数chaosからリストを取り出し、変数fruitsに代入してください
fruits = chaos[1:9]

# 変数fruitsを出力
print(fruits)


color = ["dog", "blue", "yellow"]

# 変数colorの最初の要素を「red」に更新してください
color[0] = "red"

print(color)

# リストの末尾に文字列「green」を追加してください
color.append("green")

print(color)


color = ["dog", "blue", "yellow"]
print(color)

# 変数colorの最初の要素を削除してください
del color[0]
print(color)


color = ["red", "blue", "yellow"]

# 変数colorの値が変化しないように訂正してください
color_copy = color[:]

color_copy[1] = "green"
print(color)


