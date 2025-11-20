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
        # ページを取得
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # article.product_pod を全て取得
        articles = soup.find_all('article', class_='product_pod')

        # タイトルに keyword を含むものだけ抽出
        for article in articles:
            # タイトルを取得（img の alt 属性から）
            img_tag = article.find('img')
            title = img_tag.get('alt')

            # キーワードチェック（大文字小文字を区別しない）
            if self.keyword.lower() in title.lower():
                # 画像URLを取得（相対URLを絶対URLに変換）
                img_url = img_tag.get('src')
                full_img_url = urljoin(self.base_url, img_url)

                # 価格を取得
                price = article.find('p', class_='price_color').text

                # self.books に追加
                self.books.append({
                    'title': title,
                    'image_url': full_img_url,
                    'price': price
                })

    def download_images(self):
        """画像を一括ダウンロード"""
        # book_images/ ディレクトリ作成
        save_dir = 'book_images'
        os.makedirs(save_dir, exist_ok=True)

        # 各書籍の画像をダウンロード
        for i, book in enumerate(self.books, 1):
            # タイトルを表示（長い場合は省略）
            display_title = book['title'][:40]
            print(f"[{i}/{len(self.books)}] {display_title}... ",
                  end='', flush=True)

            # 画像をダウンロード
            response = requests.get(book['image_url'], timeout=10)

            # 連番_タイトル.jpg で保存
            filename = f"{i:03d}_{book['title']}.jpg"
            filepath = os.path.join(save_dir, filename)

            # ファイルに書き込み
            with open(filepath, 'wb') as f:
                f.write(response.content)

            # レート制限（サーバーに負荷をかけないため）
            time.sleep(1)

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
