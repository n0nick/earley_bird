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

    def __str__(self):
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
    def __init__(self, routes, length):
        from parser import Parser

        self.routes = routes
        self.length = length
        self.nodes = []
        self.root = self.routes[Parser.GAMMA_SYMBOL]

        self.nodes = self.build_nodes(self.root)

    def __len__(self):
        '''Trees count'''
        return len(self.nodes)

    def __str__(self):
        '''String representation of a list of trees with indexes'''
        return '\n'.join("Parse tree #{0}:\n{1}\n\n".format(i+1, str(self.nodes[i])) for i in range(len(self)))

    def build_nodes(self, roots, start=0):
        nodes = []
        for r in roots:
            print "{0}\t\t{1}\t{2}\t{3}".format('','','', r)
            children = []
            for right in r.rule.rhs:
                if self.routes.get(right):
                    children.extend(self.build_nodes(self.routes[right], start+1))
                else: # terminal symbol - a leaf
                    children.append(TreeNode(right))

            node = TreeNode(r.rule.lhs, children)
            nodes.append(node)

        return nodes
