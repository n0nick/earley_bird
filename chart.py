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

    def add_row(self, row, parent=None):
        if not row in self.rows:
            self.rows.append(row)
        if parent:
            self.rows[self.rows.index(row)].add_parent(parent)

    def scan_routes(self, debug=False):
        from parser import Parser
        if debug:
            print "Scanning final routes..."        

        for r in self.rows:
            if r.start == 0:
                if r.is_complete():
                    if r.rule.lhs == Parser.GAMMA_SYMBOL:
                        r.mark_route(debug)


class ChartRow:
    def __init__(self, rule, dot=0, start=0):
        self.rule = rule
        self.length = len(rule)
        self.dot = dot
        self.start = start
        self.good = False
        self.parents = []

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

    def add_parent(self, parent):
        if not parent in self.parents:
            self.parents.append(parent)

    def mark_route(self, debug=False):
        if debug:
            print self

        self.good = True
        for parent in self.parents:
            parent.mark_route(debug)

