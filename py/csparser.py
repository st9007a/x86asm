import re
from oplib import Oplib

global oplib
oplib = Oplib()

class CSParser:

    def __init__(self, line):
        global oplib

        self.label = None
        self.op = None
        self.oprand_1 = {
            'value': None,
            'size': None,
            'type': None,
        }
        self.oprand_2 = {
            'value': None,
            'size': None,
            'type': None,
        }
        self.loc = None
        self.obj_code = None

        self.line = line.strip('\n')
        parse_line = [elem for elem in self.line.split(' ') if elem != '']

        if len(parse_line) == 4:
            self.label = parse_line[0]
            self.op = parse_line[1]
            self.oprand_1['value'] = parse_line[2][:-1]
            self.oprand_2['value'] = parse_line[3]

        elif len(parse_line) == 3:
            if oplib.is_op_exist(parse_line[0]):
                self.op = parse_line[0]
                self.oprand_1['value'] = parse_line[1][:-1]
                self.oprand_2['value'] = parse_line[2]
            else:
                self.label = parse_line[0]
                self.op = parse_line[1]
                self.oprand_1['value'] = parse_line[2]

        elif len(parse_line) == 2:
            self.op = parser_line[0]
            self.oprand_1['value'] = parser_line[1]

        # print self.op
        # print self.oprand_1
        # print self.oprand_2
