"""
ファイルI/O問題

ファイルの読み書きに関する基本的な操作を実装してください。
"""


def read_lines(filepath: str) -> list[str]:
    """
    ファイルを読み込んで行ごとのリストを返す
    
    各行の末尾の改行文字は削除してください。

    Args:
        filepath (str): 読み込むファイルのパス

    Returns:
        list[str]: ファイルの各行を要素とするリスト

    Examples:
        ファイル "sample.txt" の内容が:
        ```
        line1
        line2
        line3
        ```
        の場合:
        >>> read_lines("sample.txt")
        ['line1', 'line2', 'line3']
    """
    pass


def write_lines(filepath: str, lines: list[str]) -> None:
    """
    リストの各要素をファイルに1行ずつ書き込む

    Args:
        filepath (str): 書き込むファイルのパス
        lines (list[str]): 書き込む内容のリスト

    Returns:
        None

    Examples:
        >>> write_lines("output.txt", ["Hello", "World", "Python"])
        # output.txt に以下の内容が書き込まれる:
        # Hello
        # World
        # Python
    """
    pass


def count_lines(filepath: str) -> int:
    """
    ファイルの行数をカウントする

    Args:
        filepath (str): カウントするファイルのパス

    Returns:
        int: ファイルの行数

    Examples:
        >>> count_lines("sample.txt")
        3
    """
    pass


if __name__ == "__main__":
    # ここで動作確認ができます
    # テスト用のファイルを作成
    test_file = "test_sample.txt"
    test_lines = ["First line", "Second line", "Third line"]
    
    print("Writing test file...")
    write_lines(test_file, test_lines)
    
    print("Reading test file...")
    content = read_lines(test_file)
    print("Content:", content)
    
    print("Counting lines...")
    line_count = count_lines(test_file)
    print("Line count:", line_count)
