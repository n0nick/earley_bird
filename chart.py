#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

class Chart:
    def __init__(self, rows):
        '''An Earley chart is a list of rows for every input word'''
        self.rows = rows

    def __len__(self):
        '''Chart length'''
        return len(self.rows)

    def __repr__(self):
        '''Nice string representation'''
        st = '<Chart>\n\t'
        st+= '\n\t'.join(str(r) for r in self.rows)
        st+= '\n</Chart>'
        return st

    def add_row(self, row):
        '''Add a row to chart, only if wasn't already there'''
        if not row in self.rows:
            self.rows.append(row)

class ChartRow:
    def __init__(self, rule, dot=0, start=0, previous=None, completing=None):
        '''Initialize a chart row, consisting of a rule, a position
           index inside the rule, index of starting chart and
           pointers to parent rows'''
        self.rule = rule
        self.dot = dot
        self.start = start
        self.completing = completing
        self.previous = previous

    def __len__(self):
        '''A chart's length is its rule's length'''
        return len(self.rule)

    def __repr__(self):
        '''Nice string representation:
            <Row <LHS -> RHS .> [start]>'''
        rhs = list(self.rule.rhs)
        rhs.insert(self.dot, '.')
        rule_str = "[{0} -> {1}]".format(self.rule.lhs, ' '.join(rhs))
        return "<Row {0} [{1}]>".format(rule_str, self.start)

    def __cmp__(self, other):
        '''Two rows are equal if they share the same rule, start and dot'''
        if len(self) == len(other):
            if self.dot == other.dot:
                if self.start == other.start:
                    if self.rule == other.rule:
                        return 0
        return 1

    def is_complete(self):
        '''Returns true if rule was completely parsed, i.e. the dot is at the end'''
        return len(self) == self.dot

    def next_category(self):
        '''Return next category to parse, i.e. the one after the dot'''
        if self.dot < len(self):
            return self.rule[self.dot]
        return None

    def prev_category(self):
        '''Returns last parsed category'''
        if self.dot > 0:
            return self.rule[self.dot-1]
        return None

