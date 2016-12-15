import unittest
import os

import gistey.gistey as gistey


class gisteyTest(unittest.TestCase):

    def setUp(self):
        open("test_file.py", 'a').close()
        self.args = gistey.parser.parse_args(["-s",
                                              "--files", "test_file.py",
                                              "--description",
                                              "This is the description"])

    def tearDown(self):
        os.remove("test_file.py")

    def test_process_files(self):
        test_file_contents = {
            "test_file.py": {
                "content": ""
            }
        }
        self.assertEqual(gistey.process_files(self.args), test_file_contents)

    def test_construct_data(self):
        test_data = {
            "public": False,
            "description": "This is the description",
            "files": gistey.process_files(self.args)
        }
        self.assertEqual(gistey.construct_data(self.args), test_data)


if __name__ == "__main__":
    unittest.main()
