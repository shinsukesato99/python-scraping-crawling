"""
総合演習：ニュースサイトのスクレイパー

以下の機能を持つスクレイパーを作成：
1. ニュースサイトのトップページから記事一覧を取得
2. 各記事ページにアクセスして詳細情報を抽出
3. データをJSON/CSVで保存
4. エラーハンドリングとロギング
5. レート制限の実装
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import logging
from datetime import datetime
import pandas as pd

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class NewsScraper:
    """ニュースサイトのスクレイパー"""
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.articles = []
        self.session = self._create_session()
        
    def _create_session(self):
        """リトライ機能付きのセッションを作成"""
        # TODO: セッションを作成
        pass
    
    def scrape_article_list(self):
        """記事一覧を取得"""
        logger.info("記事一覧の取得を開始")
        
        try:
            # TODO: トップページから記事一覧を取得
            # TODO: 記事のURLとタイトルを抽出
            pass
            
        except Exception as e:
            logger.error(f"記事一覧の取得中にエラー: {e}")
            
        logger.info(f"{len(self.articles)} 件の記事を発見")
    
    def scrape_article_detail(self, article_url):
        """記事詳細を取得"""
        try:
            # TODO: 記事ページにアクセス
            # TODO: タイトル、本文、日付などを抽出
            # TODO: 辞書形式で返す
            pass
            
        except Exception as e:
            logger.error(f"記事詳細の取得中にエラー ({article_url}): {e}")
            return None
    
    def save_to_json(self, filename='articles.json'):
        """JSONファイルに保存"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.articles, f, ensure_ascii=False, indent=2)
            logger.info(f"データを {filename} に保存しました")
        except Exception as e:
            logger.error(f"JSON保存中にエラー: {e}")
    
    def save_to_csv(self, filename='articles.csv'):
        """CSVファイルに保存"""
        try:
            df = pd.DataFrame(self.articles)
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            logger.info(f"データを {filename} に保存しました")
        except Exception as e:
            logger.error(f"CSV保存中にエラー: {e}")
    
    def run(self):
        """スクレイピングを実行"""
        logger.info("スクレイピング開始")
        start_time = datetime.now()
        
        # 記事一覧を取得
        self.scrape_article_list()
        
        # 各記事の詳細を取得
        for i, article in enumerate(self.articles, 1):
            logger.info(f"記事 {i}/{len(self.articles)} を処理中...")
            
            detail = self.scrape_article_detail(article['url'])
            if detail:
                article.update(detail)
            
            # レート制限
            time.sleep(2)
        
        # データを保存
        self.save_to_json()
        self.save_to_csv()
        
        elapsed_time = datetime.now() - start_time
        logger.info(f"スクレイピング完了（所要時間: {elapsed_time}）")


def main():
    """メイン関数"""
    # TODO: スクレイパーを初期化
    # TODO: 実行
    
    # 例：
    # scraper = NewsScraper("https://example-news.com")
    # scraper.run()
    
    print("総合演習のテンプレートです。")
    print("base_url を設定して、各メソッドを実装してください。")


if __name__ == "__main__":
    main()
