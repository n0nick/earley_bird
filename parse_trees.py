#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

from operator import add

class TreeNode:
    def __init__(self, body, children=[]):
        self.body = body
        self.children = children

    def __len__(self):
        if self.is_leaf():
            return 1
        else:
            return reduce(add, [len(child) for child in self.children])

    def __str__(self):
        st = "[.{0} ".format(self.body)
        if not self.is_leaf():
            st+= ' '.join([str(child) for child in self.children])
        st+= ' ]'
        return st

    def is_leaf(self):
        return len(self.children) == 0

class ParseTrees:
    def __init__(self, routes, length, debug):
        self.routes = routes
        self.length = length
        self.nodes = []
        self.root = self.find_root()

        self.nodes = self.build_nodes(self.root)

    def __str__(self):
        st = []
        for i in range(len(self.nodes)):
            st.append("Parse tree #{0}:\n{1}\n\n".format(i+1, str(self.nodes[i])))
        return '\n'.join(st)

    def find_root(self):
        from parser import Parser
        return self.routes[Parser.GAMMA_SYMBOL]

    def build_nodes(self, root):
        nodes = []

        for r in root:
            children = []
            for child in r.rule.rhs:
                if child in self.routes:
                    children.extend(self.build_nodes(self.routes[child]))

            node = TreeNode(r.rule.lhs, children)
            nodes.append(node)
        
        return nodes
