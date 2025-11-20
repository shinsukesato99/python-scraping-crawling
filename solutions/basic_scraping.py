import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

# ページ取得
response = requests.get(url)
print(f"URL: {url}")
print(f"ステータスコード: {response.status_code}\n")

soup = BeautifulSoup(response.text, 'html.parser')

# すべての名言を取得
quotes = soup.find_all('div', class_='quote')

print("【課題1】すべての名言（最初の10件）\n")

# 最初の10件を表示
for i, quote in enumerate(quotes[:10], 1):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text

    print(f"{i}. {text}")
    print(f"   著者: {author}\n")

# 方法1: forループ
einstein_quotes = []
for quote in quotes:
    author = quote.find('small', class_='author').text
    if author == "Albert Einstein":
        einstein_quotes.append(quote)

# 表示
print(f"【Albert Einsteinの名言】\n")

for i, quote in enumerate(einstein_quotes, 1):
    text = quote.find('span', class_='text').text
    print(f"{i}. {text}\n")

print(f"見つかった名言: {len(einstein_quotes)}件")
