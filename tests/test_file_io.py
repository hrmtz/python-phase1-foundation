"""
ファイルI/Oのテスト

このテストは、実装が完了するまでfailします。
自分で実装を完成させてから、テストを実行してください。
"""

import pytest
import os
import tempfile
from exercises.basic.file_io import read_lines, write_lines, count_lines


class TestFileIO:
    """ファイルI/O関数のテスト"""

    def setup_method(self):
        """各テストメソッドの前に実行される"""
        # 一時ファイルを作成
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test.txt")

    def teardown_method(self):
        """各テストメソッドの後に実行される"""
        # 一時ファイルを削除
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_write_and_read_lines(self):
        """ファイルへの書き込みと読み込み"""
        lines = ["line1", "line2", "line3"]
        write_lines(self.test_file, lines)
        result = read_lines(self.test_file)
        assert result == lines, "実装してください"

    def test_read_empty_file(self):
        """空ファイルの読み込み"""
        write_lines(self.test_file, [])
        result = read_lines(self.test_file)
        assert result == [], "実装してください"

    def test_count_lines_three(self):
        """3行のファイルの行数カウント"""
        write_lines(self.test_file, ["first", "second", "third"])
        result = count_lines(self.test_file)
        assert result == 3, "実装してください"

    def test_count_lines_empty(self):
        """空ファイルの行数カウント"""
        write_lines(self.test_file, [])
        result = count_lines(self.test_file)
        assert result == 0, "実装してください"
