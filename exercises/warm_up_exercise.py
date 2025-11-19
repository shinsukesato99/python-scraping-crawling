"""
Pythonスクレイピング勉強会 - ウォーミングアップ問題
所要時間: 15分（各問題3分）

ペアで相談しながら解いてください！
"""


# ===============================================
# 問題1: FizzBuzz（3分）
# ===============================================
print("=" * 60)
print("問題1: FizzBuzz")
print("=" * 60)
print("1から30までの数字を出力。ただし、")
print("  - 3の倍数なら「Fizz」")
print("  - 5の倍数なら「Buzz」")
print("  - 3と5の両方の倍数なら「FizzBuzz」")
print()


def fizzbuzz(n):
    """1からnまでFizzBuzzを出力"""
    # TODO: 実装
    pass


# テスト実行
print("【出力結果】")
fizzbuzz(30)
print()


# ===============================================
# 問題2: リスト内の重複削除（3分）
# ===============================================
print("=" * 60)
print("問題2: リスト内の重複削除")
print("=" * 60)
print("リストから重複を削除して、ユニークな要素だけ残す")
print()

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 5]
print(f"入力: {numbers}")
print("期待される出力: [1, 2, 3, 4, 5, 6]")
print()


def remove_duplicates(lst):
    """重複を削除"""
    # TODO: 実装
    pass


# テスト実行
print("【出力結果】")
result = remove_duplicates(numbers)
print(result)
print()


# ===============================================
# 問題3: URLからドメイン名を抽出（3分）
# ===============================================
print("=" * 60)
print("問題3: URLからドメイン名を抽出")
print("=" * 60)
print("URLからドメイン名だけを取り出す")
print()

urls = [
    "https://www.example.com/page",
    "http://github.com/user/repo",
    "https://docs.python.org/3/library/",
]
print(f"入力: {urls}")
print("期待される出力: ['example.com', 'github.com', 'docs.python.org']")
print()


def extract_domain(url):
    """URLからドメイン名を抽出"""
    # TODO: 実装
    pass


# テスト実行
print("【出力結果】")
domains = [extract_domain(url) for url in urls]
print(domains)
print()


# ===============================================
# 問題4: 文字列の出現回数カウント（3分）
# ===============================================
print("=" * 60)
print("問題4: 文字列の出現回数カウント")
print("=" * 60)
print("テキスト内で各単語が何回出現するかカウント")
print()

text = "apple banana apple orange banana apple"
print(f"入力: {text}")
print("期待される出力: {{'apple': 3, 'banana': 2, 'orange': 1}}")
print()


def count_words(text):
    """単語の出現回数をカウント"""
    # TODO: 実装
    pass


# テスト実行
print("【出力結果】")
result = count_words(text)
print(result)
print()


# ===============================================
# 問題5: リストのフィルタリング（3分）
# ===============================================
print("=" * 60)
print("問題5: リストのフィルタリング")
print("=" * 60)
print("リストから偶数だけを抽出して、2倍にする")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"入力: {numbers}")
print("期待される出力: [4, 8, 12, 16, 20]")
print()


def filter_and_double(numbers):
    """偶数を抽出して2倍にする"""
    # TODO: 実装
    pass


# テスト実行
print("【出力結果】")
result = filter_and_double(numbers)
print(result)
print()


# ===============================================
# すべて完了！
# ===============================================
print("=" * 60)
print("✓ すべての問題が完了しました！")
print("次はスクレイピングの演習に進みましょう！")
print("=" * 60)
