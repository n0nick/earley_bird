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
        self.parser = parser
        self.charts = parser.charts
        self.length = len(parser)

        self.nodes = self.build_nodes(parser.complete_parses)

    def __len__(self):
        '''Trees count'''
        return len(self.nodes)

    def __repr__(self):
        '''String representation of a list of trees with indexes'''
        return '<Parse Trees>\n{0}</Parse Trees>' \
                    .format('\n'.join("Parse tree #{0}:\n{1}\n\n" \
                                        .format(i+1, str(self.nodes[i]))
                                      for i in range(len(self))))

    def build_nodes(self, roots):
        nodes = []
        for root in roots:
            children = []
            for row in root.siblings:
                if row.dot > 0:
                    if row.completing:
                        children.extend(self.build_nodes([row.completing]))
                    else:
                        children.append(TreeNode(row.prev_category()))
            node = TreeNode(root.rule.lhs, children)
            nodes.append(node)

        return nodes
