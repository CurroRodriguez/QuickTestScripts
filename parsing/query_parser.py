import pyparsing as pp
import string



class Parser(object):

    def parse(self, expression_string):
        identifier = pp.Word(pp.alphanums)
        operators = pp.Regex('=')
        operator_tokens = pp.Regex('\$eq')
        comparison_operators = operators | operator_tokens
        string_value = pp.QuotedString('"')
        numeric_value = pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?")
        boolean_value = pp.Regex('true')
        constant = string_value | numeric_value | boolean_value
        constant.setParseAction(self.replace_if_numeric, self.replace_if_boolean)
        expression = pp.Group(identifier + comparison_operators + constant)
        result = expression.parseString(expression_string)
        return result.asList()


    def replace_if_numeric(self, s=None, loc=None, toks=None):
        if toks:
            maybe_numeric = try_convert_numeric(toks[0])
            return [maybe_numeric]


    def replace_if_boolean(self, s=None, loc=None, toks=None):
        if toks:
            value = toks[0]
            if value in ['true']:
                return [True]


    




def try_convert_numeric(s):
    try:
        return float(s)
        return f if str(f) == s else int(s)
    except ValueError:
        try:
            return int(s)
        except ValueError:
            return s