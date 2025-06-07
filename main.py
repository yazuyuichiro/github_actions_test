#!/usr/bin/env python3
"""
GitHub Actions テスト用の簡易Pythonプログラム
.envファイルから環境変数を読み込み、処理を実行します
"""

import os
from dotenv import load_dotenv
import datetime

def main():
    # .envファイルから環境変数を読み込み
    load_dotenv()
    
    # 環境変数の取得
    app_name = os.getenv('APP_NAME', 'GitHub Actions Test App')
    version = os.getenv('APP_VERSION', '1.0.0')
    environment = os.getenv('ENVIRONMENT', 'development')
    
    # 現在時刻の取得
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print("=" * 50)
    print(f"🚀 {app_name} v{version}")
    print(f"📅 実行時刻: {current_time}")
    print(f"🌍 環境: {environment}")
    print("=" * 50)
    
    # 簡単な計算処理
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"🔢 数値リスト: {numbers}")
    print(f"📊 合計: {total}")
    print(f"📈 平均: {average:.2f}")
    
    print("\n✅ プログラムが正常に実行されました！")
    
    # テストが成功したことを示す
    return 0

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code) 