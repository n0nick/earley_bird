#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

from operator import add

class TreeNode:
    def __init__(self, body, children=[]):
        '''Initialize a tree with body and children'''
        self.body = body
        self.children = children

    def __len__(self):
        '''A length of a tree is its leaves count'''
        if self.is_leaf():
            return 1
        else:
            return reduce(add, [len(child) for child in self.children])

    def __repr__(self):
        '''Returns string representation of a tree in bracket notation'''
        st = "[.{0} ".format(self.body)
        if not self.is_leaf():
            st+= ' '.join([str(child) for child in self.children])
        st+= ' ]'
        return st

    def is_leaf(self):
        '''A leaf is a childless node'''
        return len(self.children) == 0

class ParseTrees:
    def __init__(self, parser):
        '''Initialize a syntax tree parsing process'''
        self.parser = parser
        self.charts = parser.charts
        self.length = len(parser)

        self.nodes = []
        for root in parser.complete_parses:
            self.nodes.extend(self.build_nodes(root))

    def __len__(self):
        '''Trees count'''
        return len(self.nodes)

    def __repr__(self):
        '''String representation of a list of trees with indexes'''
        return '<Parse Trees>\n{0}</Parse Trees>' \
                    .format('\n'.join("Parse tree #{0}:\n{1}\n\n" \
                                        .format(i+1, str(self.nodes[i]))
                                      for i in range(len(self))))

    def build_nodes(self, root):
        '''Recursively create subtree for given parse chart row'''
        nodes = []

        # find subtrees of current symbol
        if root.completing:
            down = self.build_nodes(root.completing)
        else:
            down = [TreeNode(root.prev_category())]

        # prepend subtrees of previous symbols
        prev = root.previous
        left = []
        while prev and prev.dot > 0:
            left[:0] = [self.build_nodes(prev)]
            prev = prev.previous

        left.append(down)

        return [TreeNode(root.rule.lhs, children) for children in left]

