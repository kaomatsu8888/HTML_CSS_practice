import unittest # unittestとは、Pythonの標準ライブラリで、テストを自動化するためのモジュールです。


class TestApp(unittest.TestCase):
    def test_one(self):
        actual = "Sunday"
        expected = "Monday"
        self.assertEqual(actual, expected) #結果を比較するので==ではなく、assertEqualを使う.assertの意味は「主張する」という意味です。

# python -m unittestコマンドでテストを実行する.-mの意命はmoduleを指定するという意味です。

