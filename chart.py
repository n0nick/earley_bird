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
    def __init__(self, rule, dot=0, start=0, parents=[]):
        '''Initialize a chart row, consisting of a rule, a position
           index inside the rule, index of starting chart and
           pointers to parent rows'''
        self.rule = rule
        self.dot = dot
        self.start = start
        self.parents = parents

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
        '''Two rows are equal if they share the same rule, start
           and dot'''
        if len(self) == len(other):
            if self.dot == other.dot:
                if self.start == other.start:
                    if self.rule == other.rule:
                        return 0
        return 1

    def is_complete(self):
        '''Return true if rule was completely parsed, i.e. the 'dot'
           position is at the end'''
        return len(self) == self.dot

    def next_category(self):
        '''Return next category to parse, the one in the RHS after the
           position of the 'dot'.'''
        if self.dot < len(self):
            return self.rule[self.dot]
        else:
            return None

    def add_parent(self, parent):
        '''Add a parent row if it wasn't already added'''
        if not parent in self.parents:
            self.parents.append(parent)


