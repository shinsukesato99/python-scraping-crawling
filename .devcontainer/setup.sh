#!/bin/bash

# Pythonスクレイピング勉強会 - 自動セットアップスクリプト
echo "========================================="
echo "Python Scraping Workshop セットアップ開始"
echo "========================================="

# 1. システムパッケージの更新
echo ""
echo "[1/5] システムパッケージを更新中..."
sudo apt-get update -qq

# 2. 必要なツールのインストール
echo "[2/5] 必要なツールをインストール中..."
sudo apt-get install -y -qq wget unzip curl gnupg

# 3. Google Chrome のインストール
echo "[3/5] Google Chrome をインストール中..."
if ! command -v google-chrome &> /dev/null; then
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo apt install -y -qq ./google-chrome-stable_current_amd64.deb
    rm google-chrome-stable_current_amd64.deb
    echo "✓ Google Chrome インストール完了"
else
    echo "✓ Google Chrome は既にインストールされています"
fi

# 4. ChromeDriver のインストール
echo "[4/5] ChromeDriver をインストール中..."
if ! command -v chromedriver &> /dev/null; then
    # Chrome のバージョンを取得
    CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d '.' -f 1)
    echo "  Chrome バージョン: $CHROME_VERSION"
    
    # ChromeDriver のダウンロード（Chrome for Testing を使用）
    CHROMEDRIVER_URL="https://googlechromelabs.github.io/chrome-for-testing/latest-versions-per-milestone-with-downloads.json"
    DRIVER_URL=$(curl -s $CHROMEDRIVER_URL | grep -o "https://[^\"]*linux64/chromedriver-linux64.zip" | head -1)
    
    if [ -n "$DRIVER_URL" ]; then
        wget -q "$DRIVER_URL" -O chromedriver-linux64.zip
        unzip -q chromedriver-linux64.zip
        sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
        sudo chmod +x /usr/local/bin/chromedriver
        rm -rf chromedriver-linux64.zip chromedriver-linux64
        echo "✓ ChromeDriver インストール完了"
    else
        echo "⚠ ChromeDriver の自動ダウンロードに失敗しました"
        echo "  手動でインストールしてください"
    fi
else
    echo "✓ ChromeDriver は既にインストールされています"
fi

# 5. Python パッケージのインストール
echo "[5/5] Python パッケージをインストール中..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "✓ Python パッケージ インストール完了"

# Playwright のブラウザインストール（オプション）
echo ""
echo "[オプション] Playwright ブラウザをインストール中..."
playwright install chromium --with-deps > /dev/null 2>&1
echo "✓ Playwright Chromium インストール完了"

# バージョン確認
echo ""
echo "========================================="
echo "インストール完了！"
echo "========================================="
echo ""
echo "インストールされたバージョン:"
echo "  Python: $(python --version)"
echo "  Google Chrome: $(google-chrome --version 2>/dev/null || echo 'インストール失敗')"
echo "  ChromeDriver: $(chromedriver --version 2>/dev/null || echo 'インストール失敗')"
echo ""
echo "✓ セットアップが完了しました！"
echo "  演習を開始できます: python exercises/exercise1/basic_scraping.py"
echo "========================================="
