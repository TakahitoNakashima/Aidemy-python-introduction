# coding:utf-8

# 変数townに辞書を代入してください
town = {"Aichi":"Nagoya", "Kanagawa":"Yokohama"}

# townの出力
print(town)
# 型の出力
print(type(town))

# 「Aichiの県庁所在地はNagoyaです」と出力してください
print("Aichiの県庁所在地は" + town["Aichi"] + "です")

# 「Kanagawaの県庁所在地はYokohamaです」と出力してください
print("Kanagawaの県庁所在地は" + town["Kanagawa"] + "です")

# キー「Hokkaido」、バリュー「Sapporo」を追加してください
town["Hokkaido"] = "Sapporo"
print(town)

# キー「Aichi」のバリューを「Nagoya」に変更してください
town["Aichi"] = "Nagoya"
print(town)

# キーが「Aichi」の要素を削除してください
del town["Aichi"]
print(town)

x = 5

# whileを用いて、変数xが0ではない間、ループするように作ってください
while x != 0:
    # whileの中で実行する処理は、変数xから1を引く処理と引いた後に出力させる処理です。
    x -= 1
    if x != 0:
        print(x)
    else:
        print("Bang")

numbers = [1, 2, 3, 4]

# for文を使って変数numbersの要素を出力してください
for number in numbers:
    print(number)

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number)
    # 変数numberの値が4の時に処理を終了させてください
    if number == 4:
        break

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    # 変数numberの値が2の倍数の時だけ、処理をスキップさせてください
    if number%2 == 0:
        continue
        
    print(number)

animals = ["tiger", "dog", "elephant"]

# enumerate()を用いて出力してください
for index, value in enumerate(animals):
    print(index, value)

ts = [["strawberry", "red"],
          ["peach", "pink"],
          ["banana", "yellow"]]

# for文を用いて出力してください          
for a, b in ts:
    print(a, b)

town = {"Aichi": "Nagoya", "Kanagawa": "Yokohama", "Hokkaido": "Sapporo"}

# for文を用いて出力してください
for prefecture, capital in town.items():
    print(prefecture + " " + capital)


