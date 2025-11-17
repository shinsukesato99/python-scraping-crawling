# Python スクレイピング・クローリング勉強会 - 開発環境

## 🚀 クイックスタート

### 前提条件
- Docker Desktop がインストールされていること
- VSCode がインストールされていること
- VSCode拡張機能「Dev Containers」がインストールされていること

### 環境構築手順

1. **このフォルダをVSCodeで開く**
   ```bash
   code .
   ```

2. **コマンドパレットを開く**
   - Windows/Linux: `Ctrl + Shift + P`
   - Mac: `Cmd + Shift + P`

3. **「Dev Containers: Reopen in Container」を選択**
   - コンテナのビルドと起動が自動的に行われます（初回は数分かかります）

4. **環境が起動したら準備完了！**
   - すべての必要なPythonパッケージがインストール済みです

## 📦 インストール済みパッケージ

### コアライブラリ
- `requests` - HTTP通信
- `beautifulsoup4` - HTMLパース
- `lxml` - 高速パーサー

### ブラウザ自動化
- `selenium` - ブラウザ自動化（Chrome、Firefox対応）
- `playwright` - モダンなブラウザ自動化

### データ処理
- `pandas` - データ分析・処理
- `numpy` - 数値計算

### その他
- `aiohttp` - 非同期HTTP通信
- `jupyter` - Jupyter Notebook
- `loguru` - ロギング
- `openpyxl` - Excelファイル操作

## 🧪 動作確認

コンテナ起動後、ターミナルで以下を実行して確認：

```bash
python --version
pip list
```

## 📁 プロジェクト構造

```
.
├── .devcontainer/
│   └── devcontainer.json    # Dev Container設定
├── requirements.txt          # Pythonパッケージリスト
├── scraping_workshop.md      # 勉強会資料
├── exercises/                # 演習用ディレクトリ
│   ├── exercise1/
│   ├── exercise2/
│   ├── exercise3/
│   └── exercise4/
└── README.md                 # このファイル
```

## 💻 演習の進め方

1. `exercises/` ディレクトリ内に各演習用のフォルダがあります
2. 各フォルダ内の `.py` ファイルを編集して演習を進めてください
3. ターミナルで実行：
   ```bash
   python exercises/exercise1/basic_scraping.py
   ```

## 🔧 Selenium用ChromeDriverについて

✅ **自動インストール済み**

コンテナ起動時に以下が自動的にインストールされます：
- Google Chrome
- ChromeDriver（Chrome のバージョンに対応したもの）
- Playwright Chromium

特別な設定は不要で、すぐに Selenium や Playwright を使った演習が可能です！

## 📚 勉強会資料

`scraping_workshop.md` に勉強会の詳細な資料があります。

## ⚠️ 注意事項

- スクレイピングを実行する際は、対象サイトの利用規約を必ず確認してください
- `robots.txt` を尊重してください
- サーバーに過度な負荷をかけないよう、適切な間隔を設けてください

## 🐛 トラブルシューティング

### コンテナが起動しない
- Docker Desktopが起動しているか確認
- VSCodeの「Dev Containers」拡張機能がインストールされているか確認

### パッケージが見つからない
```bash
pip install -r requirements.txt
```

### Selenium/Playwrightが動作しない
ヘッドレスモードで実行するか、必要なブラウザドライバーをインストールしてください。

## 📖 参考リンク

- [Requests Documentation](https://requests.readthedocs.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Playwright for Python](https://playwright.dev/python/)
