#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys
from Grammar import Grammar
from Parser import Parser

# TODO handle sentence from stdin
if len(sys.argv)<3:
    print "Usage: earley.py <grammar.cfg> <sentence>"
    sys.exit(1)

def read_sentence(sentence):
    return sentence.strip().split(' ')

def print_trees(trees):
    for tree in trees:
        print tree

# load grammar from file, sentence from arguments
grammar = Grammar()
grammar.readfile(sys.argv[1])
sentence = read_sentence(sys.argv[2])

# run parser
earley = Parser(grammar, sentence)
trees = earley.parse()

# print results
print_trees(trees)
