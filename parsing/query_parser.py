import pyparsing as pp



class Parser(object):

    def parse(self, expression_string):
        identifier = pp.Word(pp.alphanums)
        operators = pp.Regex('=')
        string_value = pp.QuotedString('"')
        numeric_value = pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?")
        constant = string_value | numeric_value
        expression = pp.Group(identifier + operators + constant)
        result = expression.parseString(expression_string)
        return result.asList()