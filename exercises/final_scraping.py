import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time


class BookImageDownloader:
    def __init__(self, keyword):
        self.base_url = "https://books.toscrape.com/"
        self.keyword = keyword
        self.books = []

    def search_books(self):
        """キーワードを含む書籍を検索"""
        # キーワードを含む書籍を検索して該当の書籍の画像のurlを取得
        # 松木さん・中島さんが実装
        # TODO: ページを取得
        # TODO: article.product_pod を全て取得
        # TODO: タイトルに keyword を含むものだけ抽出
        # TODO: タイトル、画像URL、価格を self.books に追加
        # self.booksの形式としては以下のような配列
        # self.books = [
        #     {
        #         'title': title,
        #         'image_url': full_img_url,
        #         'price': price
        #     })
        # ]
        pass

    def download_images(self):
        """画像を一括ダウンロード"""
        # 【10-20分】ペアB が実装
        # TODO: book_images/ ディレクトリ作成
        # TODO: 各書籍の画像をダウンロード
        # TODO: 連番_タイトル.jpg で保存
        # TODO: time.sleep(1) でレート制限
        pass

    def run(self):
        """実行"""
        # 【20-30分】ペアA が実装
        print(f"検索キーワード: '{self.keyword}'")
        self.search_books()
        print(f"発見: {len(self.books)}件")
        self.download_images()
        print("完了!")


# 実行
# タイトルに「Light」を含む本の画像をダウンロードする
downloader = BookImageDownloader("Light")
downloader.run()
