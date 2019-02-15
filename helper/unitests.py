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

    def test_remove_time(self):
        self.assertEqual("2", remove_time("  2"))
        self.assertEqual("22", remove_time("22"))
        self.assertEqual(" ", remove_time("   "))
        self.assertEqual("  ", remove_time("  "))
        self.assertEqual(" 2", remove_time(" 2"))
        self.assertEqual("", remove_time(" 2 "))
        self.assertEqual("2", remove_time(" 2 2"))

    def test_unique_values(self):
        input1 = ["2 d dsfdsfd", "2 f dsfdsfd"]
        exp1 = ["dsfdsfd"]

        self.assertEqual(exp1, list(unique_values(input1)))

        input2 = ["  fdsfdsfd"]
        exp2 = ["  fdsfdsfd"]

        self.assertEqual(exp2, unique_values(input2))

        input3 = ["fdsfdsfd", "Xfdsfdsfd"]
        exp3 = ["fdsfdsfd","Xfdsfdsfd"]

        actual = unique_values(input3)
        self.assertTrue(len(exp3) == len(actual))
        self.assertTrue(set(exp3) == set(actual))

        input4 = ["  ", "  "]
        exp4 = ["  "]
        self.assertEqual(exp4, unique_values(input4))

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
        expected = "Total of Caused by found: 1\n"

        f = io.StringIO()
        with redirect_stdout(f):
            search_string_file(lines, searched_sentence)
        s = f.getvalue()
        self.assertEqual(expected, s)

        expected = "Total of Exception found: 0\n"

        f = io.StringIO()
        with redirect_stdout(f):
            search_string_file(lines, "Exception")
        s = f.getvalue()
        self.assertEqual(expected, s)

        lines= ["Exception","Exception","Exception"]
        expected = "Total of Exception found: 3\n"

        f = io.StringIO()
        with redirect_stdout(f):
            search_string_file(lines, "Exception")
        s = f.getvalue()
        self.assertEqual(expected, s)

    def test_search_website(self):
        search_website(["Fjdemelo"], "linkedin")
        search_website(["Fjdemelo"])
        search_website(["eins", "dwei", "drei", "vier", "funf"],'', top=2)

if __name__ == '__main__':
    unittest.main()