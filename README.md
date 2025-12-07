# Python Phase 1 Foundation - 基礎トレーニング

## 目的

このリポジトリは、Python学習の「基礎体力養成」のための教材です。
Hello Worldを書いた後、Phase1のアルゴリズム練習に進む前に、
Pythonの基本的な文法と操作に慣れるための練習問題を提供します。

**重要**: このリポジトリは自力で解くことを目的としています。
解答コードは提供されていません。自分で考えて実装してください。

## 学習方針

1. **自力で解く**: 解答を見ずに、まず自分で考えて実装しましょう
2. **小さく始める**: 簡単な問題から順番に取り組みましょう
3. **テストで確認**: 実装後は必ずテストを実行して確認しましょう
4. **繰り返し練習**: 完璧にできるまで何度も挑戦しましょう

## ディレクトリ構成

```
.
├── exercises/
│   └── basic/          # 基礎練習問題
│       ├── string_reverse.py      # 文字列逆順
│       ├── character_count.py     # 文字数カウント
│       ├── list_operations.py     # リスト操作
│       ├── dictionary_operations.py  # 辞書操作
│       ├── cli_arguments.py       # CLI引数処理
│       └── file_io.py             # ファイルI/O
└── tests/              # テストコード
    ├── test_string_reverse.py
    ├── test_character_count.py
    ├── test_list_operations.py
    ├── test_dictionary_operations.py
    ├── test_cli_arguments.py
    └── test_file_io.py
```

## セットアップ

### 必要な環境

- Python 3.8 以上
- pytest（テスト実行用）

### インストール

```bash
# リポジトリをクローン
git clone <repository-url>
cd python-phase1-foundation

# pytestをインストール
pip install pytest
```

## 使い方

### 1. 問題を確認する

各練習問題ファイルを開いて、docstringに書かれた問題文を読みましょう。

```bash
# 例：文字列逆順問題を見る
cat exercises/basic/string_reverse.py
```

### 2. 実装する

`pass` の部分を自分のコードで置き換えて実装しましょう。

```python
def reverse_string(text: str) -> str:
    # ここにあなたのコードを書く
    return text[::-1]  # 例
```

### 3. 動作確認する

各ファイルは直接実行できます。

```bash
python exercises/basic/string_reverse.py
```

### 4. テストを実行する

実装が正しいか、テストで確認しましょう。

```bash
# すべてのテストを実行
pytest

# 特定のテストのみ実行
pytest tests/test_string_reverse.py

# 詳細な出力で実行
pytest -v
```

## 練習問題一覧

### 1. 文字列逆順 (string_reverse.py)
与えられた文字列を逆順にする関数を実装

### 2. 文字数カウント (character_count.py)
文字列内の特定の文字の出現回数をカウントする関数を実装

### 3. リスト操作 (list_operations.py)
- リスト内の最大値を見つける
- リストから重複を除去する

### 4. 辞書操作 (dictionary_operations.py)
- 2つの辞書をマージする
- 文字列内の単語の出現回数をカウントする

### 5. CLI引数処理 (cli_arguments.py)
コマンドライン引数をパースする関数を実装

### 6. ファイルI/O (file_io.py)
- ファイルを読み込んで行のリストを返す
- リストの内容をファイルに書き込む
- ファイルの行数をカウントする

## 学習のヒント

- **ドキュメントを読む**: Python公式ドキュメントは最良の学習資料です
- **Examples を参考にする**: 各関数のdocstringにある入出力例を参考にしましょう
- **エラーメッセージを読む**: エラーが出たら、メッセージをよく読んで原因を理解しましょう
- **一歩ずつ**: 一度に全部を解こうとせず、1つずつ確実に進めましょう

## トラブルシューティング

### pytestが見つからない場合

```bash
pip install pytest
```

### モジュールが見つからないエラー

リポジトリのルートディレクトリで実行していることを確認してください。

```bash
# ルートディレクトリに移動
cd /path/to/python-phase1-foundation

# Pythonパスを設定して実行
PYTHONPATH=. pytest
```

## 次のステップ

すべての練習問題を完了したら、Phase1のアルゴリズム練習に進みましょう！
基礎がしっかりしていれば、より高度な問題にも取り組めます。

## ライセンス

このリポジトリは学習目的で自由に使用できます。