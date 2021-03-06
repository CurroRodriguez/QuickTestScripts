import unittest

import query_parser

class TestFilterQueryExpression(unittest.TestCase):
    
    def test_provides_expression_components(self):
        expression = query_parser.FilterQueryExpression('name', '=', 'foo')
        self.assertEqual(expression.identifier, 'name')
        self.assertEqual(expression.operator, '=')
        self.assertEqual(expression.value, 'foo')

class TestParserWithReplacer(unittest.TestCase):
    
    def test_callback_is_invoked(self):
        parser = query_parser.ParserWithReplacer()
        result = parser.parse('name="foo"')
        qry_expression = result[0]
        self.assertEqual(qry_expression.identifier, 'name')
        self.assertEqual(qry_expression.operator, '=')
        self.assertEqual(qry_expression.value, 'foo')
    

class TestParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.parser = query_parser.Parser()
        return super(TestParser, cls).setUpClass()


    def test_parses_string_filter(self):
        self.given('id="id"')
        self.expect(['id', '=', 'id'])


    def test_parses_integer_values(self):
        self.given('id=1')
        self.expect(['id', '=', 1])
        


    def test_parses_floats(self):
        self.given('elevation=2.345')
        self.expect(['elevation', '=', 2.345])


    def test_parses_negative_floats(self):
        self.given('elevation=-3.21')
        self.expect(['elevation', '=', -3.21])


    def test_parses_boolean_value(self):
        self.given('visible=true')
        self.expect(['visible', '=', True])


    def test_parses_equality_operator(self):
        self.given('id$eq"id"')
        self.expect(['id', '$eq', 'id'])


    def test_allows_compound_statements(self):
        self.given('id="1"$orelevation=3.2')
        self.expect([['id', '=', 1], '$or', ['elevation', '=', 3.2]])




    def given(self, expression):
        self.expression = expression


    def expect(self, expected):
        expected_list = [expected]
        self.actual = self.parser.parse(self.expression)
        self.assertListEqual(self.actual, expected_list)



class TestTryConvertNumeric(unittest.TestCase):

    def test_returns_string_if_not_numeric(self):
        self.given('asdf')
        self.expect('asdf')


    def test_returns_integer_if_integer_string(self):
        self.given('1')
        self.expect(1)


    def test_returns_negative_integer(self):
        self.given('-3')
        self.expect(-3)


    def test_returns_float_if_float_string(self):
        self.given('1.2')
        self.expect(1.2)


    def test_returns_negative_float(self):
        self.given('-1.2')
        self.expect(-1.2)


    def test_returns_float_with_precision(self):
        self.given('1.10')
        self.expect(1.1)



    def given(self, s):
        self.str_value = s


    def expect(self, expected):
        actual = query_parser.try_convert_numeric(self.str_value)
        self.assertEqual(actual, expected)




if __name__=='__main__':
    unittest.main()