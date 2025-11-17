"""
演習3：動的コンテンツのスクレイピング
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


def exercise3_1():
    """演習3-1：Seleniumの基本操作"""
    print("=== 演習3-1：Seleniumの基本操作 ===")
    
    # ヘッドレスモードで実行（オプション）
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # TODO: WebDriverを初期化
    # TODO: ページを開く
    # TODO: 要素が表示されるまで待機
    # TODO: 要素を取得
    # TODO: ブラウザを閉じる
    
    pass


def exercise3_2():
    """演習3-2：スクロールと動的読み込み"""
    print("\n=== 演習3-2：スクロールと動的読み込み ===")
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # TODO: ページを開く
    # TODO: ページの最下部までスクロール
    # TODO: 新しいコンテンツが読み込まれるまで待機
    # TODO: これを繰り返す
    # TODO: すべてのアイテムを取得
    
    pass


if __name__ == "__main__":
    print("注意: Seleniumを実行するには、ChromeDriverのインストールが必要です。")
    print("詳細はREADME.mdを参照してください。\n")
    
    exercise3_1()
    exercise3_2()
