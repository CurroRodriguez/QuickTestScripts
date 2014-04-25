import pyparsing as pp
import string



class Parser(object):

    def parse(self, expression_string):
        result = self.grammar.parseString(expression_string)
        return result.asList()


    @property
    def grammar(self):
        return  (self.compound_expression 
                |self.expression)


    @property
    def identifier(self):
        return pp.Word(pp.alphanums)


    @property
    def numeric_operators(self):
        return pp.Regex('=')


    @property
    def operator_tokens(self):
        return pp.Regex('\$eq')


    @property 
    def logical_operator(self):
        return pp.Regex('\$or')


    @property
    def string_value(self):
        return pp.QuotedString('"')


    @property
    def numeric_value(self):
        return pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?")


    @property
    def boolean_value(self):
        return pp.Regex('true')


    @property
    def expression(self):
        comparison_operators = self.numeric_operators | self.operator_tokens
        constant = self.string_value | self.numeric_value | self.boolean_value
        constant.setParseAction(self.replace_if_numeric, self.replace_if_boolean)
        return pp.Group(self.identifier + comparison_operators + constant)


    @property
    def compound_expression(self):
        return pp.Group(self.expression + self.logical_operator + self.expression)


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
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s