#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

from chart import *
from grammar import *

class Parser:
    GAMMA_SYMBOL = 'GAMMA'

    def __init__(self, grammar, sentence):
        self.grammar = grammar
        self.sentence = sentence
        self.length = len(sentence)
        self.charts = [Chart([]) for i in range(self.length+1)]

    def init_first_chart(self):
        row = ChartRow(Rule(Parser.GAMMA_SYMBOL, ['S']), 0, 0)
        self.charts[0].add_row(row)

    def prescan(self, chart, position):
        word = self.sentence[position-1]
        if word:
            rules = [Rule(tag, [word.word]) for tag in word.tags]
            for rule in rules:
                chart.add_row(ChartRow(rule, 1, position-1))

    def predict(self, chart, position):
        for row in chart.rows:
            next_cat = row.next_category()
            rules = self.grammar[next_cat]
            if rules:
                for rule in rules:
                    new = ChartRow(rule, 0, position, [row])
                    chart.add_row(new)

    def complete(self, chart, position):
        for row in chart.rows:
            if row.is_complete():
                completed = row.rule.lhs
                for r in self.charts[row.start].rows:
                    if completed == r.next_category():
                        new = ChartRow(r.rule, r.dot+1, r.start, [row, r])
                        chart.add_row(new)

    def parse(self, debug=False):
        self.init_first_chart()

        i = 0
        while i < len(self.charts):
            chart = self.charts[i]
            self.prescan(chart, i)

            length = len(chart)
            old_length = -1
            while old_length != length:
                self.predict(chart, i)
                self.complete(chart, i)

                old_length = length
                length = len(chart)

            i+= 1              
        
        if debug:
            self.print_charts()

    def routes(self, debug):
        if debug:
            print "Scanning final routes..."
        self.charts[-1].scan_routes(debug)

    def print_charts(self):
        print "Parsing charts:"
        for i in range(len(self.charts)):
            print "-----------{0}-----------".format(i)
            print self.charts[i]
            print "-------------------------".format(i)
