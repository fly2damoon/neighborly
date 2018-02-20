import json
import re

class Rule():
    def __init__(self, rule):
        self.properties = rule
        self.op_greater_than = "GREATER_THAN"
        self.op_equal_to = "EQUAL_TO"
        self.op_or = "OR"
        self.op_and = "AND"
        self.op_regex_match = "REGEX_MATCH"
        self.op_length = "LENGTH"

    #properties
    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def name(self):
        return self.properties.get('name', "")

    @property
    def rule(self):
        return self.properties.get('rule', {})

    @property
    def oper(self):
        return [Oper(self.rule)]

    def evaluate(self, user_input):
        self.user_input = user_input
        return self.evaluate_operands(self.oper)

    def evaluate_operands(self, items):
        eval = []
        for item in items:
            if item.operator == self.op_greater_than:
                ret = self.evaluate_operands(item.operands)
                eval.append(int(ret[0]) > int(ret[1]))
            elif item.operator == self.op_equal_to:
                ret = self.evaluate_operands(item.operands)
                eval.append(int(ret[0]) == int(ret[1]))
            elif item.operator == self.op_or:
                evals = self.evaluate_operands(item.operands)
                result = False
                for val in evals:
                    result = result or val
                eval.append(result)
            elif item.operator == self.op_and:
                evals = self.evaluate_operands(item.operands)
                result = True
                for val in evals:
                    result = result and val
                eval.append(result)
            elif item.operator == self.op_regex_match:
                eval.append(self.evaluate_regex_match(item))
            elif item.operator == self.op_length:
                field = self.get_field_value(item)
                eval.append(len(field))
            else:
                eval.append(item.value)

        return eval

    def get_field_value(self, item):
        field_value = item.get_field()

        # TODO : validation on field_value
        fields = field_value.split('.')
        input = self.user_input

        # TODO Validation on dict get if value is None
        for field in fields:
            input = input.get(field)

        return input

    def evaluate_regex_match(self, item):
        sequence = self.get_field_value(item)
        pattern = item.get_value()
        #print "regex : ", sequence, pattern,  re.match(pattern, sequence)

        # TODO: regex value in the sample is not working. Need a valid regex pattern.
        return re.match(pattern, sequence)

class Oper():
    def __init__(self, oper):
        self.properties = oper


    @property
    def operator(self):
        return self.properties.get('operator', '')

    @property
    def operands(self):
        if self.properties.get('operands') is None:
            return None

        result = []
        for item in self.properties.get('operands', []):
            result.append(Oper(item))
        return result

    def get_field(self):
        # TODO array validation
        # TODO field can be on operands 0
        if self.operands is None:
            return None

        for operand in self.operands:
            if operand.field is not None:
                return operand.field

        return None

    def get_value(self):
        # TODO array validation
        # TODO value can be on operands 0
        if self.operands is None:
            return None

        for operand in self.operands:
            if operand.value is not None:
                return operand.value

        return None

    @property
    def field(self):
        return self.properties.get('field', None)

    @property
    def value(self):
        return self.properties.get('value', None)
