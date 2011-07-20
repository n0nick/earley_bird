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

    def scan_routes(self, debug=False):
        from parser import Parser

        for row in self.rows:
            rule = row.rule
            if rule.lhs == Parser.GAMMA_SYMBOL:
                if row.start == 0:  
                    if row.is_complete():
                        row.mark_route(debug)


class ChartRow:
    def __init__(self, rule, dot=0, start=0, parents=[]):
        self.rule = rule
        self.dot = dot
        self.start = start
        self.good = False
        self.parents = parents

    def __len__(self):
        return len(self.rule)

    def __repr__(self):
        rhs = list(self.rule.rhs)
        rhs.insert(self.dot, '*')
        rule_str = "[{0} -> {1}]".format(self.rule.lhs, ' '.join(rhs))
        return "<Row {0} [{1}]>".format(rule_str, self.start, self.parents)

    def __cmp__(self, other):
        if len(self) == len(other):
            if self.dot == other.dot:
                if self.start == other.start:
                    if self.rule == other.rule:
                        return 0
        return 1

    def is_complete(self):
        return len(self) == self.dot

    def next_category(self):
        if self.dot < len(self):
            return self.rule[self.dot]
        else:
            return None

    def add_parent(self, parent):
        if not parent in self.parents:
            self.parents.append(parent)

    def mark_route(self, debug=False):
        if debug:
            print self

        self.good = True
        for parent in self.parents:
            parent.mark_route(debug)

