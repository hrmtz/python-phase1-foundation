"""
リスト操作問題

リストに関する基本的な操作を実装してください。
"""


def find_max(numbers: list[int]) -> int:
    """
    リスト内の最大値を見つける

    Args:
        numbers (list[int]): 整数のリスト（空でない）

    Returns:
        int: 最大値

    Examples:
        >>> find_max([1, 2, 3, 4, 5])
        5
        >>> find_max([5, 4, 3, 2, 1])
        5
        >>> find_max([10])
        10
        >>> find_max([-5, -2, -10, -1])
        -1
    """
    pass


def remove_duplicates(items: list) -> list:
    """
    リストから重複を除去する（順序は保持）

    Args:
        items (list): 任意の要素のリスト

    Returns:
        list: 重複を除去したリスト

    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 3, 3])
        [1, 2, 3]
        >>> remove_duplicates(["a", "b", "a", "c"])
        ['a', 'b', 'c']
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1, 1])
        [1]
    """
    pass


if __name__ == "__main__":
    # ここで動作確認ができます
    print(find_max([1, 2, 3, 4, 5]))
    print(find_max([5, 4, 3, 2, 1]))
    print(find_max([10]))
    print(find_max([-5, -2, -10, -1]))
    
    print(remove_duplicates([1, 2, 2, 3, 3, 3]))
    print(remove_duplicates(["a", "b", "a", "c"]))
    print(remove_duplicates([]))
    print(remove_duplicates([1, 1, 1, 1]))
