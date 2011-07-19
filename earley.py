#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys
from grammar import *
from sentence import *
from parser import *

# TODO handle sentence from stdin
if len(sys.argv)<3:
    print "Usage: earley.py <grammar.cfg> <sentence>"
    sys.exit(1)

def print_trees(trees):
    for tree in trees:
        print tree

# load grammar from file, sentence from arguments
grammar = Grammar.from_file(sys.argv[1])
sentence = Sentence.from_string(sys.argv[2])

# run parser
earley = Parser(grammar, sentence)
earley.parse()
#trees = earley.parse()

# print results
# print_trees(trees)
