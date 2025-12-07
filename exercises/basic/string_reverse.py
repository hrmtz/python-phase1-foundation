"""
文字列逆順問題

与えられた文字列を逆順にして返す関数を実装してください。
"""


def reverse_string(text: str) -> str:
    """
    文字列を逆順にする

    Args:
        text (str): 入力文字列

    Returns:
        str: 逆順にした文字列

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
        >>> reverse_string("a")
        'a'
    """
    pass


if __name__ == "__main__":
    # ここで動作確認ができます
    print(reverse_string("hello"))
    print(reverse_string("Python"))
    print(reverse_string(""))
    print(reverse_string("a"))
