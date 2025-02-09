import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cli import create_parser, main


class TestCLI(unittest.TestCase):
    def setUp(self): 
        self.parser = create_parser()

    def test_analyze_command(self):
        args = self.parser.parse_args(["analyze", "test_dir"])
        self.assertEqual(args.command, "analyze")
        self.assertEqual(args.directory, "test_dir")

    def test_rename_command(self):
        args = self.parser.parse_args(["rename", "test_dir"])
        self.assertEqual(args.command, "rename")
        self.assertEqual(args.directory, "test_dir")

    def test_copy_command(self):
        args = self.parser.parse_args(["copy", "source_dir", "target_dir"])
        self.assertEqual(args.command, "copy")
        self.assertEqual(args.source, "source_dir")
        self.assertEqual(args.target, "target_dir")

if __name__ == '__main__':
    unittest.main()