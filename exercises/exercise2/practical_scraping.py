"""
演習2：実践的なスクレイピング
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def exercise2_1():
    """演習2-1：テーブルデータの抽出"""
    print("=== 演習2-1：テーブルデータの抽出 ===")
    
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    
    # TODO: ページを取得
    # TODO: テーブルを見つける
    # TODO: 行と列を解析
    # TODO: DataFrameに変換
    # TODO: CSVに保存
    
    pass


def exercise2_2():
    """演習2-2：複数ページのクローリング"""
    print("\n=== 演習2-2：複数ページのクローリング ===")
    
    base_url = "https://example.com/page/"
    all_data = []
    
    # TODO: ページ1〜5まで順番にアクセス
    # TODO: 各ページからデータを抽出
    # TODO: リクエスト間に適切な待機時間を設ける
    # TODO: すべてのデータを統合
    
    pass


if __name__ == "__main__":
    exercise2_1()
    exercise2_2()
