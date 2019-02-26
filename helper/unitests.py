#Yes, unitests is not a good name

from main import *
from functions import *

import sys

import unittest
import io
import sys

class TestFunctions(unittest.TestCase):

    def test_search(self):
        sub_string = "world"
        lines=["world","hello","hi"]

        self.assertEqual(len(search(lines, sub_string)),1)

        sub_string = "tchau"
        lines = ["world", "hello", "hi"]

        self.assertEqual(search(lines, sub_string), [])

        sub_string = "world"
        lines = ["world", "world", "world"]

        self.assertEqual(len(search(lines, sub_string)),3 )

        sub_string = "world"
        lines = []
        self.assertEqual(len(search(lines, sub_string)),0)


    #search function:
    def test_print_l(self):
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            print_l(["lines"])
        s = f.getvalue()
        self.assertEqual(s, "lines\n")

        f = io.StringIO()
        with redirect_stdout(f):
            print_l(["xx","xx","xx"])
        s = f.getvalue()
        self.assertEqual(s, "xx\nxx\nxx\n")

    def test_unique_values(self):
        inp = ["fdsfdsfd", "fdsfdsfd"]
        exp = ["fdsfdsfd"]

        self.assertEqual("fdsfdsfd", unique_values(inp))

        input = ["fdsfdsfd"]
        exp = ["fdsfdsfd"]

        self.assertEqual(unique_values(input), "fdsfdsfd")

        input = ["fdsfdsfd", "Xfdsfdsfd"]
        exp = ["fdsfdsfd","Xfdsfdsfd"]

        self.assertEqual(unique_values(input), "fdsfdsfd")

    def test_find_all(self):
        self.assertEqual(0, find_all("vcxvcx", "vcxvcx")[0])
        self.assertEqual([], find_all("vcxvcx", "fdsfdsfs"))
        self.assertEqual(0, find_all("vcxfc", "vcx")[0])
        self.assertEqual(3, find_all("vcxfc", "fc")[0])
        self.assertEqual([], find_all("CC", "CCCC"))
        self.assertEqual(0, find_all("vcxvcx", "v")[0])

    def test_search_string_file(self):
        from contextlib import redirect_stdout
        #Test 1
        lines = ["DIDO", "DIDO", "Caused by"]
        searched_sentence = "Caused by"
        flag_unique = False
        expected = "Total of 'Caused by' found: 1\n"

        f = io.StringIO()
        with redirect_stdout(f):
            search_string_file(lines, searched_sentence, flag_unique)
        s = f.getvalue()
        self.assertEqual(expected, s)

    def test_search_website(self):
        search_website(["Fjdemelo"], "linkedin")
        search_website(["Fjdemelo"])
        search_website(["eins", "dwei", "drei", "vier", "funf"],'', top=2)

if __name__ == '__main__':
    unittest.main()