"""
文字数カウントのテスト

このテストは、実装が完了するまでfailします。
自分で実装を完成させてから、テストを実行してください。
"""

import pytest
from exercises.basic.character_count import count_character


class TestCountCharacter:
    """文字数カウント関数のテスト"""

    def test_count_l_in_hello(self):
        """helloの中のlの数"""
        assert count_character("hello", "l") == 2, "実装してください"

    def test_count_o_in_hello(self):
        """helloの中のoの数"""
        assert count_character("hello", "o") == 1, "実装してください"

    def test_count_not_found(self):
        """存在しない文字のカウント"""
        assert count_character("hello", "x") == 0, "実装してください"

    def test_count_in_empty_string(self):
        """空文字列でのカウント"""
        assert count_character("", "a") == 0, "実装してください"

    def test_count_repeated_character(self):
        """繰り返し文字のカウント"""
        assert count_character("aaaaaa", "a") == 6, "実装してください"
