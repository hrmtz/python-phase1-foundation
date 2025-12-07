"""
CLI引数処理問題

コマンドライン引数を処理する関数を実装してください。
"""


def parse_arguments(args: list[str]) -> dict:
    """
    コマンドライン引数をパースする
    
    "--key value" 形式の引数を辞書に変換します。
    "--" で始まる引数をキー、次の引数を値とします。

    Args:
        args (list[str]): コマンドライン引数のリスト

    Returns:
        dict: パースされた引数の辞書

    Examples:
        >>> parse_arguments(["--name", "Alice", "--age", "25"])
        {'name': 'Alice', 'age': '25'}
        >>> parse_arguments(["--file", "data.txt"])
        {'file': 'data.txt'}
        >>> parse_arguments([])
        {}
        >>> parse_arguments(["--verbose", "true", "--debug", "false"])
        {'verbose': 'true', 'debug': 'false'}
    """
    pass


if __name__ == "__main__":
    import sys
    
    # コマンドライン引数をパースして表示
    if len(sys.argv) > 1:
        parsed = parse_arguments(sys.argv[1:])
        print("Parsed arguments:", parsed)
    else:
        # テスト用のサンプル実行
        print(parse_arguments(["--name", "Alice", "--age", "25"]))
        print(parse_arguments(["--file", "data.txt"]))
        print(parse_arguments([]))
        print(parse_arguments(["--verbose", "true", "--debug", "false"]))
