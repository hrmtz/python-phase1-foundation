"""
文字列逆順のテスト

このテストは、実装が完了するまでfailします。
自分で実装を完成させてから、テストを実行してください。
"""

import pytest
from exercises.basic.string_reverse import reverse_string


class TestReverseString:
    """文字列逆順関数のテスト"""

    def test_reverse_simple_string(self):
        """シンプルな文字列の逆順"""
        assert reverse_string("hello") == "olleh", "実装してください"

    def test_reverse_python(self):
        """Pythonという文字列の逆順"""
        assert reverse_string("Python") == "nohtyP", "実装してください"

    def test_reverse_empty_string(self):
        """空文字列の逆順"""
        assert reverse_string("") == "", "実装してください"

    def test_reverse_single_character(self):
        """1文字の逆順"""
        assert reverse_string("a") == "a", "実装してください"

    def test_reverse_numbers(self):
        """数字を含む文字列の逆順"""
        assert reverse_string("12345") == "54321", "実装してください"
