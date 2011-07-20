#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

from operator import add

class TreeNode:
    def __init__(self, body, children=[]):
        self.body = body
        self.children = children

    def leaves_count(self):
        if self.is_leaf():
            return 1
        else:
            return reduce(add, [child.leaves_count() for child in self.children])

    def is_leaf(self):
        return self.children == []

class ParseTrees:
    def __init__(self, routes, length, debug):
        self.routes = routes
        self.nodes = [list() for i in range(length)]
        self.trees = []
        self.length = length

#        self.build_trees(debug)

    def build_nodes(self, debug=None):
        for row in self.routes:
            rule = row.rule
            children = [TreeNode(s) for s in rule.rhs]
            node = TreeNode(rule.lhs, children)
            self.nodes[rule.start].append(node)
        if debug:
            print "Created nodes:"
            print self.nodes
    
    def build_trees(self, nodes, debug=None):
        self.build_nodes(debug)
        trees = None #TODO
        res = []
        if trees:
            for tree in trees:
                if tree.leaves_count == self.length:
                    res.append(tree)
        return res
