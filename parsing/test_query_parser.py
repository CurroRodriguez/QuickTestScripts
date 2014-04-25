import unittest

import query_parser

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = query_parser.Parser()
        return super(TestParser, cls).setUpClass()


    def test_parses_string_filter(self):
        self.given('id="id"')
        self.expect(['id', '=', 'id'])


    def test_parses_numeric_filter(self):
        self.given('id=1')
        self.expect(['id', '=', '1'])



    def given(self, expression):
        self.expression = expression


    def expect(self, expected):
        expected_list = [expected]
        actual = self.parser.parse(self.expression)
        self.assertListEqual(actual, expected_list)




if __name__=='__main__':
    unittest.main()