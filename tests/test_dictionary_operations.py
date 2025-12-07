"""
辞書操作のテスト

このテストは、実装が完了するまでfailします。
自分で実装を完成させてから、テストを実行してください。
"""

import pytest
from exercises.basic.dictionary_operations import merge_dicts, count_words


class TestMergeDicts:
    """辞書マージ関数のテスト"""

    def test_merge_different_keys(self):
        """異なるキーの辞書マージ"""
        result = merge_dicts({"a": 1, "b": 2}, {"c": 3})
        assert result == {"a": 1, "b": 2, "c": 3}, "実装してください"

    def test_merge_overlapping_keys(self):
        """重複するキーの辞書マージ"""
        result = merge_dicts({"a": 1}, {"a": 2})
        assert result == {"a": 2}, "実装してください"

    def test_merge_with_empty_dict(self):
        """空辞書とのマージ"""
        result = merge_dicts({}, {"x": 10})
        assert result == {"x": 10}, "実装してください"

    def test_merge_empty_with_nonempty(self):
        """空でない辞書と空辞書のマージ"""
        result = merge_dicts({"x": 10}, {})
        assert result == {"x": 10}, "実装してください"


class TestCountWords:
    """単語カウント関数のテスト"""

    def test_count_words_with_duplicates(self):
        """重複する単語のカウント"""
        result = count_words("hello world hello")
        assert result == {"hello": 2, "world": 1}, "実装してください"

    def test_count_words_unique(self):
        """ユニークな単語のカウント"""
        result = count_words("one two three")
        assert result == {"one": 1, "two": 1, "three": 1}, "実装してください"

    def test_count_words_empty_string(self):
        """空文字列の単語カウント"""
        result = count_words("")
        assert result == {}, "実装してください"

    def test_count_words_all_same(self):
        """全て同じ単語のカウント"""
        result = count_words("test test test")
        assert result == {"test": 3}, "実装してください"
