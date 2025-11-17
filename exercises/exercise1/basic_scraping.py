"""
演習1：requestsとBeautifulSoupの基本
"""

import requests
from bs4 import BeautifulSoup


def exercise1_1():
    """演習1-1：シンプルなHTML取得"""
    print("=== 演習1-1：シンプルなHTML取得 ===")
    
    url = "https://httpbin.org/html"
    
    # TODO: requestsでHTMLを取得
    # TODO: ステータスコードを確認
    # TODO: HTMLの内容を表示
    
    pass


def exercise1_2():
    """演習1-2：特定の要素を抽出"""
    print("\n=== 演習1-2：特定の要素を抽出 ===")
    
    url = "https://httpbin.org/html"
    response = requests.get(url)
    
    # TODO: BeautifulSoupでHTMLをパース
    # TODO: すべてのh1タグを取得
    # TODO: すべてのaタグからhref属性を取得
    
    pass


def exercise1_3():
    """演習1-3：CSSセレクタを使った抽出"""
    print("\n=== 演習1-3：CSSセレクタを使った抽出 ===")
    
    url = "https://example.com"
    response = requests.get(url)
    
    # TODO: 特定のクラスを持つdivを取得
    # TODO: IDで要素を取得
    # TODO: 階層構造を指定して取得
    
    pass


if __name__ == "__main__":
    exercise1_1()
    exercise1_2()
    exercise1_3()
