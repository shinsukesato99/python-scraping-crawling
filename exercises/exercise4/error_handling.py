"""
演習4：エラーハンドリングとベストプラクティス
"""

import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from functools import wraps
from datetime import datetime, timedelta


def exercise4_1():
    """演習4-1：堅牢なスクレイパーの作成"""
    print("=== 演習4-1：堅牢なスクレイパーの作成 ===")
    
    def create_session():
        """リトライ機能付きのセッションを作成"""
        # TODO: リトライ戦略を設定
        # TODO: セッションにアダプターをマウント
        pass
    
    def scrape_with_error_handling(url):
        """エラーハンドリング付きのスクレイピング"""
        # TODO: User-Agentを設定
        # TODO: タイムアウトを設定
        # TODO: 例外処理を実装
        pass
    
    # テスト
    url = "https://httpbin.org/html"
    # scrape_with_error_handling(url)


def exercise4_2():
    """演習4-2：レート制限の実装"""
    print("\n=== 演習4-2：レート制限の実装 ===")
    
    class RateLimiter:
        """レート制限を管理するクラス"""
        def __init__(self, max_requests, time_window):
            # TODO: 初期化
            pass
        
        def __call__(self, func):
            # TODO: デコレータを実装
            pass
    
    # 使用例：10秒間に最大5リクエスト
    # @RateLimiter(max_requests=5, time_window=10)
    def fetch_page(url):
        response = requests.get(url)
        print(f"Fetched: {url} at {datetime.now()}")
        return response
    
    # テスト
    # for i in range(8):
    #     fetch_page(f"https://httpbin.org/delay/0")


if __name__ == "__main__":
    exercise4_1()
    exercise4_2()
