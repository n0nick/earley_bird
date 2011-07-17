#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

class ChartRow:
    def __init__(self, rule, position, start_index):
        self.rule = rule
        self.length = len(rule)
        self.position = position
        self.start_index = start_index

    def __str__(self):
        return "<row {0} [{1}]>".format(self.rule, self.start_index)

    def is_complete(self):
        self.length == self.position

class Parser:
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
        self.chart = self.init_chart()

    def init_chart(self):
        rules = self.grammar.rules_for('S')
        return [ChartRow(rule, 0, 0) for rule in rules]

    def predict(self, row):
        r = row.rule
        rules = self.grammar.rules_for(r.rhs[row.position])
        if rules:
            for o in rules:
                new = ChartRow(o, 0, row.position)
                self.chart.append(new)

    def scan(self, row):
        rule = row.rule
        if rule.is_terminal():
            rule_word = rule[0]
            input_word = self.sentence[row.position]
            if rule_word == input_word:
                new = ChartRow(rule, row.position+1, row.start_index+1)
                self.chart.append(new)
                return True
        return False

    def complete(self, row):
        if row.is_complete():
            lhs = row.rule.lhs

            for r in self.chart:
                if r.start_index == row.start_index:
                    if r.rule.is_terminal():
                        continue
                    if r.is_complete():
                        continue

    def parse(self):
        i = 0
        while i < len(self.chart):
            row = self.chart[i]
            print row
            if not self.complete(row):
                if not self.scan(row):
                    self.predict(row)
            i+= 1

        return [False]

