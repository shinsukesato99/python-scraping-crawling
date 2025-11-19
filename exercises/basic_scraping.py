import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

# TODO: ページを取得（requests.get）
# TODO: ステータスコードを確認（requests.getの結果からstatus_codeを取得）
# TODO: HTMLをパース（BeautifulSoup(response.text, 'html.parser')）

# 【課題1】すべての名言を取得して表示
# TODO: すべての名言（class="quote"）を取得（前段で取得したHTMLをパースした結果からfind???で取得できる）
# TODO: 各名言から以下を表示（あとは前段で取得した内容を表示する）
#   - 名言テキスト
#   - 著者名

print("\n" + "="*60)
print("【課題2】特定の著者でフィルタリング")
print("="*60 + "\n")

# 時間余れば【課題2】Albert Einsteinの名言だけをフィルタリング
# TODO: Albert Einsteinの名言だけを抽出
# TODO: 見つかった名言を表示
