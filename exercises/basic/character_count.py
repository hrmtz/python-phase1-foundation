"""
文字数カウント問題

与えられた文字列内に特定の文字が何回出現するかカウントする関数を実装してください。
"""


def count_character(text: str, char: str) -> int:
    """
    文字列内の特定の文字の出現回数をカウントする

    Args:
        text (str): 検索対象の文字列
        char (str): カウントする文字（1文字）

    Returns:
        int: 文字の出現回数

    Examples:
        >>> count_character("hello", "l")
        2
        >>> count_character("hello", "o")
        1
        >>> count_character("hello", "x")
        0
        >>> count_character("", "a")
        0
        >>> count_character("aaaaaa", "a")
        6
    """
    pass


if __name__ == "__main__":
    # ここで動作確認ができます
    print(count_character("hello", "l"))
    print(count_character("hello", "o"))
    print(count_character("hello", "x"))
    print(count_character("", "a"))
    print(count_character("aaaaaa", "a"))
