# GitHub Actions テストプロジェクト

## 概要
このプロジェクトは、GitHub Actionsの基本的な動作を確認するための簡易的なPythonアプリケーションです。

## 機能
- `.env`ファイルから環境変数を読み込み
- 現在時刻の表示
- 簡単な計算処理の実行
- GitHub Actionsでの自動テスト実行

## 必要な環境
- Python 3.8以上
- pip

## セットアップ

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. 環境変数ファイルの作成
`.env`ファイルを作成し、以下の内容を設定してください：

```env
APP_NAME=GitHub Actions Test App
APP_VERSION=2.1.0
ENVIRONMENT=development
DEBUG=false
LOG_LEVEL=info
```

### 3. アプリケーションの実行
```bash
python main.py
```

## GitHub Actions
このプロジェクトでは、以下のGitHub Actionsワークフローを設定しています：

- **テスト**: Python 3.8, 3.9, 3.10, 3.11での動作確認
- **デプロイ**: mainブランチへのプッシュ時の自動デプロイメント処理

## ディレクトリ構成
```
.
├── main.py              # メインアプリケーション
├── requirements.txt     # Python依存関係
├── .env                # 環境変数（Git管理対象外）
├── .gitignore          # Git除外設定
├── README.md           # このファイル
└── .github/
    └── workflows/
        └── ci.yml      # GitHub Actions設定
```

## 使用技術
- Python 3.x
- python-dotenv
- GitHub Actions

## ライセンス
MIT License

---
**最終更新**: GitHub Actions テスト実行中 🚀 