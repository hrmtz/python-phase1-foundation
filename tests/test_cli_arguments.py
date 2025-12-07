"""
CLI引数処理のテスト

このテストは、実装が完了するまでfailします。
自分で実装を完成させてから、テストを実行してください。
"""

import pytest
from exercises.basic.cli_arguments import parse_arguments


class TestParseArguments:
    """CLI引数パース関数のテスト"""

    def test_parse_two_arguments(self):
        """2つの引数のパース"""
        result = parse_arguments(["--name", "Alice", "--age", "25"])
        assert result == {"name": "Alice", "age": "25"}, "実装してください"

    def test_parse_single_argument(self):
        """1つの引数のパース"""
        result = parse_arguments(["--file", "data.txt"])
        assert result == {"file": "data.txt"}, "実装してください"

    def test_parse_empty_arguments(self):
        """空の引数リストのパース"""
        result = parse_arguments([])
        assert result == {}, "実装してください"

    def test_parse_boolean_like_arguments(self):
        """真偽値のような引数のパース"""
        result = parse_arguments(["--verbose", "true", "--debug", "false"])
        assert result == {"verbose": "true", "debug": "false"}, "実装してください"
