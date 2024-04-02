func = lambda a, b: (b + 1, a * 2) #lambda式がよく理解できない
x, y = 1, 2 #x, yに1, 2を代入
x, y = func(x, y) #func(x, y)の返り値をx, yに代入
print(x, y) #x, yを出力
