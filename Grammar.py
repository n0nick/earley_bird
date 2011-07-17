#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys

class Rule:
    def __init__(self, lhs, rhs, grammar):
        self.lhs = lhs
        self.rhs = rhs
        self.grammar = grammar

    def __len__(self):
        return len(self.rhs)

    def __str__(self):
        return "{0} -> {1}".format(self.lhs, ' | '.join(self.rhs))

    def __getitem__(self, item):
        return self.rhs[item]

    def is_terminal(self):
        return len(self) == 1 and self.rhs[0] in self.grammar.terminals

class Grammar:
    def __init__(self):
        self.grammar = {}
        self.symbols = set()
        self.terminals = set()
        self.nonterminals = set()

    def readfile(self, filename):
        "reads grammar from file"
        # TODO move this out of here
        try:
            lines = file(filename)
        except IOError as e:
            sys.stderr.write("Error reading file {0}\n".format(filename))
            sys.exit(1)

        for line in lines:
            if line[0] == '#' or len(line) < 3: # comment
                continue

            # lhs -> outcome | outcome | outcome
            rule = line.split('->')
            lhs = rule[0].strip()
            for outcome in rule[1].split('|'):
                symbols = outcome.strip().split(' ')
                r = Rule(lhs, symbols, self)
                for sym in symbols:
                    self.symbols.add(sym)

            self.nonterminals.add(lhs)
            self.symbols.add(lhs)

            self.add_rule(r)
       
        self.terminals = self.symbols.difference(self.nonterminals)

        return self

    def add_rule(self, rule):
        lhs = rule.lhs
        if lhs in self.grammar:
            self.grammar[lhs].extend(rule)
        else:
            self.grammar[lhs] = [rule]

    def rules_for(self, lhs):
        if lhs in self.grammar:
            return self.grammar[lhs]
        else:
            return None

