"""
リスト操作のテスト

このテストは、実装が完了するまでfailします。
自分で実装を完成させてから、テストを実行してください。
"""

import pytest
from exercises.basic.list_operations import find_max, remove_duplicates


class TestFindMax:
    """最大値検索関数のテスト"""

    def test_find_max_ascending(self):
        """昇順リストの最大値"""
        assert find_max([1, 2, 3, 4, 5]) == 5, "実装してください"

    def test_find_max_descending(self):
        """降順リストの最大値"""
        assert find_max([5, 4, 3, 2, 1]) == 5, "実装してください"

    def test_find_max_single_element(self):
        """1要素のリストの最大値"""
        assert find_max([10]) == 10, "実装してください"

    def test_find_max_negative_numbers(self):
        """負の数を含むリストの最大値"""
        assert find_max([-5, -2, -10, -1]) == -1, "実装してください"


class TestRemoveDuplicates:
    """重複除去関数のテスト"""

    def test_remove_duplicates_numbers(self):
        """数値リストの重複除去"""
        assert remove_duplicates([1, 2, 2, 3, 3, 3]) == [1, 2, 3], "実装してください"

    def test_remove_duplicates_strings(self):
        """文字列リストの重複除去"""
        assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"], "実装してください"

    def test_remove_duplicates_empty_list(self):
        """空リストの重複除去"""
        assert remove_duplicates([]) == [], "実装してください"

    def test_remove_duplicates_all_same(self):
        """全て同じ要素のリストの重複除去"""
        assert remove_duplicates([1, 1, 1, 1]) == [1], "実装してください"
