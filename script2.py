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

vege = "potato"
numbers = [4, 5, 2, 7, 6]

# 変数vegeのオブジェクトの長さを出力してください
print(len(vege))

# 変数numbersのオブジェクトの長さを出力してください
print(len(numbers))

animal = "elephant"

# 変数animal_bigに変数animalに格納された文字列を大文字にしたものを代入してください
animal_big = animal.upper()

print(animal)
print(animal_big)

# 変数animalに「e」が何個存在するか出力してください
print(animal.count("e"))

fruit = "banana"
color = "yellow"

# 「bananaはyellowです」と出力してください
print("{}は{}です".format(fruit, color))

n = [3, 6, 8, 6, 3, 2, 4, 6]

# 「2」のインデックス番号を出力してください
print(n.index(2))

# 変数n内の「6」の数を出力してください
print(n.count(6))


n = [53, 26, 37, 69, 24, 2]

# nをソートし、数字が小さい順になるように出力してください
n.sort()
print(n)

# 数字が小さい順になるようにソートされたnの要素の順番を反対にし、数字が大きい順になるように出力してください
n.reverse()
print(n)


# 「Yamadaです」と出力する関数introduceを作ってください
def introduce():
    print("Yamadaです")


# 関数の呼び出し
introduce()

# 引数nを用いて、引数を３乗した値を出力する関数cube_calを作ってください 
def cube_cal(n):
    print(n ** 3)


# 関数の呼び出し
cube_cal(4)

# 関数introduceを作ってください
def introduce(name, age):
    print(name + "です。" + age + "歳です。")

# 関数の呼び出し
introduce("Yamada", "18")

# 初期値を設定してください
def introduce(age, name = "Yamada"):
    print(name + "です。" + str(age) + "歳です。")

# 関数の呼び出し
introduce(18)


# bmiを計算する関数を作り、bmiの値を返り値としてください
def bmi(height, weight):
    result = weight / height ** 2
    return result

print(bmi(1.65, 65))

# fromを利用してtimeをインポートしてください
from time  import time 

# now_timeに現在の時刻を代入してください
now_time = time()

print(now_time)


# MyProductクラスを定義
class MyProduct:
    # コンストラクタを修正してください
    def __init__(self, name, price, stock):
        # 引数をメンバに格納してください
        self.name = name
        self.price = price
        self.stock = stock
        
        self.sales = 0
        
# MyProductを呼び出し、オブジェクトproduct_1を作成
product_1 = MyProduct("cake", 500, 20)

# product_1のstockを出力してください
print(product_1.stock)


# MyProductクラスを定義
class MyProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.sales = 0
    # 概要メソッド
    def summary(self):
        message = "called summary().\n name: " + self.get_name() + \
        "\n price: " + str(self.price) + \
        "\n stock: " + str(self.stock) + \
        "\n sales: " + str(self.sales)
        print(message)
    # nameを返すget_name()を作成して下さい
    def get_name(self):
        return self.name
    # 引数のぶんだけpriceを減らすdiscount()を作成して下さい
    def discount(self, n):
        self.price -= n

product_2 = MyProduct("phone", 30000, 100)
# 5000だけdiscountして下さい
product_2.discount(5000)

# product_2のsummaryを出力して下さい
product_2.summary()

def bmi(height, weight):
    return weight / height**2

# 「bmiは＊＊です」と出力させてください
print("bmiは%.4fです" % bmi(170, 65))


