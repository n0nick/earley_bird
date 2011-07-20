#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys

class Rule:
    def __init__(self, lhs, rhs):
        '''Initializes grammar rule: LHS -> [RHS]'''
        self.lhs = lhs
        self.rhs = rhs

    def __len__(self):
        '''A rule's length is its RHS's length'''
        return len(self.rhs)

    def __repr__(self):
        '''Nice string representation'''
        return "<Rule {0} -> {1}>".format(self.lhs, ' '.join(self.rhs))

    def __getitem__(self, item):
        '''Return a member of the RHS'''
        return self.rhs[item]

    def __cmp__(self, other):
        '''Rules are equal iff both their sides are equal'''
        if self.lhs == other.lhs:
            if self.rhs == other.rhs:
                return 0
        return 1

class Grammar:
    def __init__(self):
        '''A grammar is a collection of rules, sorted by LHS'''
        self.rules = {}

    def __repr__(self):
        '''Nice string representation'''
        st = '<Grammar>\n'
        for group in self.rules.values():
            for rule in group:
                st+= '\t{0}\n'.format(str(rule))
        st+= '</Grammar>'
        return st

    def __getitem__(self, lhs):
        '''Return rules for a given LHS'''
        if lhs in self.rules:
            return self.rules[lhs]
        else:
            return None

    def add_rule(self, rule):
        '''Add a rule to the grammar'''
        lhs = rule.lhs
        if lhs in self.rules:
            self.rules[lhs].append(rule)
        else:
            self.rules[lhs] = [rule]

    @staticmethod
    def from_file(filename):
        '''Returns a Grammar instance created from a text file.
           The file lines should have the format:
               lhs -> outcome | outcome | outcome'''

        grammar = Grammar()
        for line in open(filename):
            # ignore comments
            line = line[0:line.find('#')]
            if len(line) < 3:
                continue

            rule = line.split('->')
            lhs = rule[0].strip()
            for outcome in rule[1].split('|'):
                rhs = outcome.strip()
                symbols = rhs.split(' ') if rhs else []
                r = Rule(lhs, symbols)
                grammar.add_rule(r)

        return grammar

