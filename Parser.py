#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

class ChartRow:
    def __init__(self, rule, position, start=0, end=0):
        self.rule = rule
        self.length = len(rule)
        self.position = position
        self.start = start
        self.end = end

    def __str__(self):
        rule_str = self.rule.__str__().split(' ')
        rule_str.insert(self.position+2, '*')
        return "<row {0} [{1}]>".format(' '.join(rule_str), self.start)

    def is_complete(self):
        self.length == self.position

class Parser:
    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
        self.charts = [list() for i in range(len(sentence)+1)]
        self.init_chart()

    def init_chart(self):
        rules = self.grammar.rules_for('S')
        self.charts[0] = [ChartRow(rule, 0, 0) for rule in rules]

    def predict(self, row):
        r = row.rule
        print '\tPREDICT?'
        if not r.is_terminal() and not row.is_complete():
            print '\tPREDICT!'
            rules = self.grammar.rules_for(r.rhs[row.position])
            if rules:
                for o in rules:
                    new = ChartRow(o, 0, row.end, row.end)
                    self.charts[new.end].append(new)

    def scan(self, row):
        rule = row.rule
        print '\tSCAN?'
        if rule.is_terminal():
            rule_word = rule[0]
            input_word = self.sentence[row.position]
            print "\t\t{0} = {1} ?".format(rule_word, input_word)
            if rule_word == input_word:
                print '\t\tSCAN!'
                new = ChartRow(rule, row.position+1, row.start, row.end+1)
                self.charts[new.end].append(new)
                return True
        return False

    def complete(self, row):
        print '\tCOMPLETE?'
        if row.is_complete():
            lhs = row.rule.lhs

            for current in self.charts[row.start]:
                if current.start == row.start:
                    print '\t\tCOMPLETE!'
                    if current.rule.is_terminal():
                        continue
                    if current.is_complete():
                        continue

                    current_symbol = current.rule[current.position]

                    if row.rule.lhs == current_symbol:
                        new = ChartRow(current.rule, current.position+1, current.start, current.end)
                        self.charts[new.end].append(new)
            return True
        return False

    def parse(self):
        i = 0
        while i < len(self.charts):
            row = self.charts[i]
            print row
            if not self.complete(row):
                if not self.scan(row):
                    self.predict(row)
            i+= 1

        return [False]

