class Duck:
    def __init__(self):
        self.birdsong = 'ガーガー'

    def sing(self):
        birdsong = 'カーカー'
        print(birdsong)
        print(self.birdsong)
        self.birdsong = 'ピヨピヨ'
        print(self.birdsong)
        print(birdsong)


duck = Duck()
duck.sing()

# 実行結果の順番解説
# 1. birdsong = 'カーカー'
# 2. print(birdsong) -> カーカー
# 3. print(self.birdsong) -> ガーガー
# 4. self.birdsong = 'ピヨピヨ'
# 5. print(self.birdsong) -> ピヨピヨ
# 6. print(birdsong) -> カーカー
# 7. print(self.birdsong) -> ピヨピヨ

