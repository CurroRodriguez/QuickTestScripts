import pyparsing as pp
import string


class FilterQueryExpression(object):
    
    def __init__(self, identifier, operator, value):
        self._identifier = identifier
        self._operator = operator
        self._value = value
        
        
    @property
    def identifier(self):
        return self._identifier
        
    
    @property
    def operator(self):
        return self._operator
        
        
    @property
    def value(self):
        return self._value


class ParserWithReplacer(object):

    def parse(self, qry_str):
        result = self.expression.parseString(qry_str)
        return result.asList()


    @property
    def expression(self):
        expression = pp.Group(self.identifier + self.string_operators + self.string_value)
        expression.setParseAction(self.make_query_expression)
        return expression
    
    @property
    def string_value(self):
        expression = pp.QuotedString('"')
        return expression


    @property
    def identifier(self):
        expression = pp.Word(pp.alphas)
        return expression
        
    @property
    def string_operators(self):
        expression = pp.Regex('=')
        return expression
        
        
    def make_query_expression(self, s=None, loc=None, toks=None):
        if toks:
            expression = toks[0]
            qry_expression = FilterQueryExpression(expression[0], expression[1], expression[2])
            return [qry_expression]



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