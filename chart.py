#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

class Chart:
    def __init__(self, rows):
        self.rows = rows

    def __len__(self):
        return len(self.rows)

    def __str__(self):
        return '\n'.join(str(r) for r in self.rows)

    def has_row(self, row): #TODO
        res = False
        for r in self.rows:
            if row == r:
                res = True
                break
        return res

    def add_row(self, row):
        if not self.has_row(row):
            self.rows.append(row)

class ChartRow:
    def __init__(self, rule, dot=0, start=0):
        self.rule = rule
        self.length = len(rule)
        self.dot = dot
        self.start = start

    def __str__(self):
        rule_str = str(self.rule).split(' ')
        rule_str.insert(self.dot + 2, '*')
        return "<row {0} [{1}]>".format(' '.join(rule_str), self.start)

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

