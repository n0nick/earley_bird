#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

class Chart:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __repr__(self):
        st = '<Chart>\n\t'
        st+= '\n\t'.join(str(r) for r in self.rows)
        st+= '\n</Chart>'
        return st

    def add_row(self, row):
        if not row in self.rows:
            self.rows.append(row)

class ChartRow:
    def __init__(self, rule, dot=0, start=0):
        self.rule = rule
        self.length = len(rule)
        self.dot = dot
        self.start = start

    def __repr__(self):
        rhs = list(self.rule.rhs)
        rhs.insert(self.dot, '*')
        rule_str = "[{0} -> {1}]".format(self.rule.lhs, ' '.join(rhs))

        return "<Row {0} [{1}]>".format(rule_str, self.start)

    def __cmp__(self, other):
        if self.length == other.length:
            if self.dot == other.dot:
                if self.start == other.start:
                    if self.rule == other.rule:
                        return 0
        return 1

    def is_complete(self):
        return self.length == self.dot

    def next_category(self):
        if self.dot < self.length:
            return self.rule[self.dot]
        else:
            return None

