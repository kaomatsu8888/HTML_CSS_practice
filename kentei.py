def divide(number, divider):
    try:
        answer = number / divider
        return answer
    except ZeroDivisionError:
        print('0で割ることはできません。')
    except TypeError:
        print('引数の型が不正です')
    finally:
        print("--finally処理--")

answer = divide(50.0, 0)
print(f"結果: {answer}")

# 処理の流れ
# divide関数を定義する
#   引数numberとdividerを受け取る
#   try節を開始する
#     numberをdividerで割る
#     answerに代入する
#     answerを返す
#   except節を開始する
#     ZeroDivisionErrorが発生した場合
#       0で割ることはできません。を表示する
#   except節を開始する
#     TypeErrorが発生した場合
#       引数の型が不正ですを表示する
#   finally節を開始する
#     --finally処理--を表示する
# divide関数に50.0と0を渡して実行する
#   0で割ることはできません。を表示する
#   --finally処理--を表示する
#   結果: Noneを表示する

