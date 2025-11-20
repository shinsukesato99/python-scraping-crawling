"""
Pythonスクレイピング勉強会 - ウォーミングアップ問題【解答例】
所要時間: 15分（各問題3分）
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
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:  # 3と5の両方の倍数（先に判定）
            result.append("FizzBuzz")
        elif i % 3 == 0:  # 3の倍数
            result.append("Fizz")
        elif i % 5 == 0:  # 5の倍数
            result.append("Buzz")
        else:
            result.append(str(i))

    print(", ".join(result))


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
    # 方法1: setを使う（最も簡単・順序は保証されない）
    return sorted(list(set(lst)))

    # 方法2: 順序を保持したい場合
    # unique = []
    # for item in lst:
    #     if item not in unique:
    #         unique.append(item)
    # return unique

    # 方法3: dict.fromkeys()を使う（順序保持・Python 3.7+）
    # return list(dict.fromkeys(lst))


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
    # 方法1: 文字列操作（シンプル）
    url = url.replace("https://", "").replace("http://", "")
    url = url.replace("www.", "")
    domain = url.split("/")[0]
    return domain

    # 方法2: urllib.parseを使う（より正確）
    # from urllib.parse import urlparse
    # parsed = urlparse(url)
    # domain = parsed.netloc.replace("www.", "")
    # return domain


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
    # 方法1: 辞書を使う
    words = text.split()
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

    # 方法2: getを使う（よりPythonicな方法）
    # words = text.split()
    # count = {}
    # for word in words:
    #     count[word] = count.get(word, 0) + 1
    # return count

    # 方法3: Counterを使う（最も簡単）
    # from collections import Counter
    # return dict(Counter(text.split()))


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
    # 方法1: forループ
    result = []
    for num in numbers:
        if num % 2 == 0:  # 偶数判定
            result.append(num * 2)
    return result

    # 方法2: リスト内包表記（Pythonicな方法）
    # return [num * 2 for num in numbers if num % 2 == 0]

    # 方法3: filter + map（関数型プログラミング風）
    # return list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))


# テスト実行
print("【出力結果】")
result = filter_and_double(numbers)
print(result)
print()


# ===============================================
# ボーナス: 各問題の複数解法まとめ
# ===============================================
print("=" * 60)
print("📚 学習ポイント")
print("=" * 60)
print("""
問題1 (FizzBuzz):
  - 条件分岐の順序が重要（15の倍数を先に判定）
  - % 演算子で割り算の余りを求める

問題2 (重複削除):
  - set() は順序を保証しない
  - dict.fromkeys() は順序を保持（Python 3.7+）
  - 用途に応じて使い分ける

問題3 (URL処理):
  - 文字列操作で簡単に実装可能
  - urllib.parse を使うとより正確
  - スクレイピングで実際に使う技術！

問題4 (カウント):
  - 辞書は頻度カウントに便利
  - collections.Counter が最も簡単
  - get() メソッドでデフォルト値を指定

問題5 (フィルタリング):
  - リスト内包表記がPythonicで読みやすい
  - filter + map も関数型プログラミングの基本
  - 用途に応じて選択
""")

print("=" * 60)
print("✓ すべての問題が完了しました！")
print("次はスクレイピングの演習に進みましょう！")
print("=" * 60)
