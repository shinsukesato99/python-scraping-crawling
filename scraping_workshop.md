# Pythonスクレイピング・クローリング勉強会

## 📋 勉強会の概要

**対象者**: Webアプリケーションエンジニア
**所要時間**: 約3時間
**形式**: 演習中心（理論20% / 実践80%）

---

## 🎯 学習目標

- Pythonを使った基本的なスクレイピング技術の習得
- requests、BeautifulSoup、Seleniumの使い分け
- クローリング時のマナーとベストプラクティスの理解
- 実務で使える実践的なスクレイピングスキルの獲得

---

## 🛠 事前準備

### 必要な環境
```bash
# Python 3.8以上
python --version

# 必要なライブラリのインストール
pip install requests beautifulsoup4 lxml selenium pandas
pip install playwright  # 任意
```

### 推奨ツール
- VSCode または PyCharm
- Chrome または Firefox ブラウザ
- ChromeDriver（Selenium用）

---

## 📚 第1部：スクレイピングの基礎（45分）

### 1-1. スクレイピングとは

**スクレイピング（Scraping）**
- Webページから必要な情報を抽出する技術
- HTML/CSSの構造を解析してデータを取得

**クローリング（Crawling）**
- 複数のWebページを自動的に巡回する技術
- リンクを辿ってページを収集

### 1-2. 法的・倫理的注意点

⚠️ **重要な注意事項**
- `robots.txt`を確認し、遵守する
- 利用規約を確認する
- サーバーに過度な負荷をかけない（適切な間隔を空ける）
- 著作権・個人情報に配慮する
- 商用利用の場合は特に注意

---

## 💻 演習1：requestsとBeautifulSoupの基本（30分）

### 演習1-1：シンプルなHTML取得

**課題**: 指定したURLからHTMLを取得して表示する

```python
import requests
from bs4 import BeautifulSoup

# 練習用URL（例：httpbin.org）
url = "https://httpbin.org/html"

# TODO: requestsでHTMLを取得
# TODO: ステータスコードを確認
# TODO: HTMLの内容を表示
```

<details>
<summary>解答例</summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://httpbin.org/html"

response = requests.get(url)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    print(response.text[:500])  # 最初の500文字を表示
```
</details>

### 演習1-2：特定の要素を抽出

**課題**: HTMLから見出し（h1, h2）とリンク（a）を抽出する

```python
# TODO: BeautifulSoupでHTMLをパース
# TODO: すべてのh1タグを取得
# TODO: すべてのaタグからhref属性を取得
```

<details>
<summary>解答例</summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://httpbin.org/html"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# h1タグを取得
h1_tags = soup.find_all('h1')
for h1 in h1_tags:
    print(f"H1: {h1.text.strip()}")

# すべてのリンクを取得
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text.strip()
    print(f"Link: {text} -> {href}")
```
</details>

### 演習1-3：CSSセレクタを使った抽出

**課題**: CSSセレクタを使って特定のクラスやIDの要素を取得する

```python
# TODO: 特定のクラスを持つdivを取得
# TODO: IDで要素を取得
# TODO: 階層構造を指定して取得
```

<details>
<summary>解答例</summary>

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com"  # 適切なURLに変更
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# クラスで取得
elements = soup.select('.class-name')

# IDで取得
element = soup.select_one('#element-id')

# 階層構造で取得
elements = soup.select('div.container > p.text')
```
</details>

---

## 💻 演習2：実践的なスクレイピング（45分）

### 演習2-1：テーブルデータの抽出

**課題**: Wikipediaのテーブルからデータを抽出してCSVに保存

練習用URL: `https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)`

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"

# TODO: ページを取得
# TODO: テーブルを見つける
# TODO: 行と列を解析
# TODO: DataFrameに変換
# TODO: CSVに保存
```

<details>
<summary>解答例</summary>

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# テーブルを取得
table = soup.find('table', {'class': 'wikitable'})

# ヘッダーを取得
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# データ行を取得
rows = []
for tr in table.find_all('tr')[1:]:  # ヘッダー行をスキップ
    cells = tr.find_all(['td', 'th'])
    row = [cell.text.strip() for cell in cells]
    if row:
        rows.append(row)

# DataFrameに変換
df = pd.DataFrame(rows, columns=headers[:len(rows[0])])
print(df.head())

# CSVに保存
df.to_csv('countries_population.csv', index=False, encoding='utf-8')
```
</details>

### 演習2-2：複数ページのクローリング

**課題**: ページネーションがあるサイトから複数ページのデータを取得

```python
import requests
from bs4 import BeautifulSoup
import time

base_url = "https://example.com/page/"
all_data = []

# TODO: ページ1〜5まで順番にアクセス
# TODO: 各ページからデータを抽出
# TODO: リクエスト間に適切な待機時間を設ける
# TODO: すべてのデータを統合
```

<details>
<summary>解答例</summary>

```python
import requests
from bs4 import BeautifulSoup
import time

base_url = "https://example.com/page/"
all_data = []

for page_num in range(1, 6):
    url = f"{base_url}{page_num}"
    print(f"Scraping page {page_num}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # データを抽出（実際の構造に合わせて変更）
        items = soup.select('.item')
        for item in items:
            data = {
                'title': item.select_one('.title').text.strip(),
                'description': item.select_one('.description').text.strip(),
            }
            all_data.append(data)
        
        # サーバーに負荷をかけないよう待機
        time.sleep(2)
        
    except Exception as e:
        print(f"Error on page {page_num}: {e}")

print(f"Total items scraped: {len(all_data)}")
```
</details>

---

## 💻 演習3：動的コンテンツのスクレイピング（40分）

### 3-1. Seleniumの基本

JavaScriptで動的に生成されるコンテンツはrequests+BeautifulSoupでは取得できません。
Seleniumを使うと、実際のブラウザを操作してJavaScript実行後のHTMLを取得できます。

### 演習3-1：Seleniumの基本操作

**課題**: Seleniumでブラウザを起動し、ページを操作する

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TODO: WebDriverを初期化
# TODO: ページを開く
# TODO: 要素が表示されるまで待機
# TODO: 要素を取得
# TODO: ブラウザを閉じる
```

<details>
<summary>解答例</summary>

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# ヘッドレスモードで実行（オプション）
chrome_options = Options()
chrome_options.add_argument('--headless')

# WebDriverを初期化
driver = webdriver.Chrome(options=chrome_options)

try:
    # ページを開く
    driver.get("https://example.com")
    
    # 要素が表示されるまで待機（最大10秒）
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
    )
    
    # 要素を取得
    print(element.text)
    
    # すべての段落を取得
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for p in paragraphs:
        print(p.text)
        
finally:
    # ブラウザを閉じる
    driver.quit()
```
</details>

### 演習3-2：スクロールと動的読み込み

**課題**: 無限スクロールのページからデータを取得

```python
from selenium import webdriver
import time

# TODO: ページを開く
# TODO: ページの最下部までスクロール
# TODO: 新しいコンテンツが読み込まれるまで待機
# TODO: これを繰り返す
# TODO: すべてのアイテムを取得
```

<details>
<summary>解答例</summary>

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://example.com/infinite-scroll")
    
    # スクロールを繰り返す
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    for _ in range(5):  # 5回スクロール
        # 最下部までスクロール
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # 新しいコンテンツの読み込みを待機
        time.sleep(2)
        
        # 新しい高さを取得
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # すべてのアイテムを取得
    items = driver.find_elements(By.CSS_SELECTOR, ".item")
    print(f"Total items: {len(items)}")
    
    for item in items:
        print(item.text)
        
finally:
    driver.quit()
```
</details>

---

## 💻 演習4：エラーハンドリングとベストプラクティス（30分）

### 演習4-1：堅牢なスクレイパーの作成

**課題**: リトライ機能とエラーハンドリングを実装

```python
import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# TODO: リトライ戦略を設定
# TODO: タイムアウトを設定
# TODO: User-Agentを設定
# TODO: 例外処理を実装
```

<details>
<summary>解答例</summary>

```python
import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    """リトライ機能付きのセッションを作成"""
    session = requests.Session()
    
    # リトライ戦略
    retry = Retry(
        total=3,
        read=3,
        connect=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504)
    )
    
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session

def scrape_with_error_handling(url):
    """エラーハンドリング付きのスクレイピング"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    session = create_session()
    
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # データを抽出
        title = soup.find('h1')
        if title:
            print(f"Title: {title.text.strip()}")
        else:
            print("Title not found")
            
        return soup
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    
    return None

# 実行例
url = "https://example.com"
result = scrape_with_error_handling(url)
```
</details>

### 演習4-2：レート制限の実装

**課題**: 適切な間隔でリクエストを送信する仕組みを実装

```python
import time
from functools import wraps

# TODO: デコレータでレート制限を実装
# TODO: 1秒あたりのリクエスト数を制御
```

<details>
<summary>解答例</summary>

```python
import time
from functools import wraps
from datetime import datetime, timedelta

class RateLimiter:
    """レート制限を管理するクラス"""
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window  # 秒
        self.requests = []
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.now()
            
            # 古いリクエスト記録を削除
            self.requests = [
                req_time for req_time in self.requests
                if now - req_time < timedelta(seconds=self.time_window)
            ]
            
            # レート制限チェック
            if len(self.requests) >= self.max_requests:
                sleep_time = (
                    self.requests[0] + timedelta(seconds=self.time_window) - now
                ).total_seconds()
                if sleep_time > 0:
                    print(f"Rate limit reached. Sleeping for {sleep_time:.2f}s")
                    time.sleep(sleep_time)
                    self.requests = []
            
            # リクエストを記録
            self.requests.append(datetime.now())
            
            return func(*args, **kwargs)
        return wrapper

# 使用例：10秒間に最大5リクエスト
@RateLimiter(max_requests=5, time_window=10)
def fetch_page(url):
    response = requests.get(url)
    print(f"Fetched: {url} at {datetime.now()}")
    return response

# テスト
for i in range(8):
    fetch_page(f"https://httpbin.org/delay/0")
```
</details>

---

## 🎓 第5部：実践プロジェクト（30分）

### 総合演習：ニュースサイトのスクレイパー

**課題**: 以下の機能を持つスクレイパーを作成

1. ニュースサイトのトップページから記事一覧を取得
2. 各記事ページにアクセスして詳細情報を抽出
3. データをJSON/CSVで保存
4. エラーハンドリングとロギング
5. レート制限の実装

```python
import requests
from bs4 import BeautifulSoup
import json
import time
import logging
from datetime import datetime

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class NewsScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.articles = []
        
    def scrape_article_list(self):
        """記事一覧を取得"""
        # TODO: 実装
        pass
    
    def scrape_article_detail(self, article_url):
        """記事詳細を取得"""
        # TODO: 実装
        pass
    
    def save_to_json(self, filename):
        """JSONファイルに保存"""
        # TODO: 実装
        pass
    
    def run(self):
        """スクレイピングを実行"""
        # TODO: 実装
        pass

# 実行
if __name__ == "__main__":
    scraper = NewsScraper("https://example-news.com")
    scraper.run()
```

---

## 📖 参考資料・ツール

### 推奨ライブラリ

- **requests**: HTTP通信
- **BeautifulSoup4**: HTMLパース
- **lxml**: 高速パーサー
- **Selenium**: ブラウザ自動化
- **Playwright**: モダンなブラウザ自動化
- **Scrapy**: 本格的なクローリングフレームワーク
- **pandas**: データ処理

### デバッグ・開発ツール

- Chrome DevTools（要素の検証）
- Selector Gadget（CSSセレクタ生成）
- Postman（APIテスト）

### 学習リソース

- [Requests公式ドキュメント](https://requests.readthedocs.io/)
- [BeautifulSoup公式ドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium公式ドキュメント](https://selenium-python.readthedocs.io/)

---

## ✅ チェックリスト

勉強会終了時に確認：

- [ ] requestsで基本的なHTTP通信ができる
- [ ] BeautifulSoupで要素を抽出できる
- [ ] CSSセレクタを使いこなせる
- [ ] 複数ページをクローリングできる
- [ ] Seleniumで動的コンテンツを取得できる
- [ ] エラーハンドリングができる
- [ ] レート制限を実装できる
- [ ] スクレイピングの法的・倫理的側面を理解している

---

## 💡 次のステップ

1. **Scrapyの学習**: より本格的なクローリングフレームワーク
2. **非同期処理**: aiohttp、asyncioで高速化
3. **データ保存**: データベース（MongoDB、PostgreSQL）への保存
4. **定期実行**: cron、Airflowでの自動化
5. **クラウド化**: AWS Lambda、Google Cloud Functionsでの運用

---

## ❓ Q&A

よくある質問と回答：

**Q: スクレイピングは違法ですか？**
A: スクレイピング自体は違法ではありませんが、利用規約違反や著作権侵害には注意が必要です。

**Q: JavaScriptで読み込まれるコンテンツが取得できません**
A: Seleniumや Playwrightを使用してブラウザをエミュレートしてください。

**Q: 503エラーが頻発します**
A: リクエストの間隔を空ける、User-Agentを設定する、robots.txtを確認してください。

---

**勉強会担当者**: [名前]
**作成日**: 2024年
**バージョン**: 1.0
