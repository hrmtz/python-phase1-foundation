"""
辞書操作問題

辞書（dict）に関する基本的な操作を実装してください。
"""


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    2つの辞書をマージする（dict2の値が優先される）

    Args:
        dict1 (dict): 最初の辞書
        dict2 (dict): 2番目の辞書

    Returns:
        dict: マージされた辞書

    Examples:
        >>> merge_dicts({"a": 1, "b": 2}, {"c": 3})
        {'a': 1, 'b': 2, 'c': 3}
        >>> merge_dicts({"a": 1}, {"a": 2})
        {'a': 2}
        >>> merge_dicts({}, {"x": 10})
        {'x': 10}
        >>> merge_dicts({"x": 10}, {})
        {'x': 10}
    """
    pass


def count_words(text: str) -> dict:
    """
    文字列内の各単語の出現回数をカウントする

    Args:
        text (str): スペース区切りの単語を含む文字列

    Returns:
        dict: 単語をキー、出現回数を値とする辞書

    Examples:
        >>> count_words("hello world hello")
        {'hello': 2, 'world': 1}
        >>> count_words("one two three")
        {'one': 1, 'two': 1, 'three': 1}
        >>> count_words("")
        {}
        >>> count_words("test test test")
        {'test': 3}
    """
    pass


if __name__ == "__main__":
    # ここで動作確認ができます
    print(merge_dicts({"a": 1, "b": 2}, {"c": 3}))
    print(merge_dicts({"a": 1}, {"a": 2}))
    print(merge_dicts({}, {"x": 10}))
    print(merge_dicts({"x": 10}, {}))
    
    print(count_words("hello world hello"))
    print(count_words("one two three"))
    print(count_words(""))
    print(count_words("test test test"))
