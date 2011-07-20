#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys
from grammar import *
from sentence import *
from parser import *
from parse_trees import *

def print_trees(trees):
    if trees:
        for tree in trees:
            print tree

def run():
    if len(sys.argv)<3:
        print "Usage: earley.py <grammar.cfg> <sentence> [--debug]"
        sys.exit(1)

    # load grammar from file, sentence from arguments
    grammar = Grammar.from_file(sys.argv[1])
    sentence = Sentence.from_string(sys.argv[2])
    debug = len(sys.argv)==4 and sys.argv[3] == '--debug'

    # run parser
    earley = Parser(grammar, sentence)
    earley.parse(debug)

    routes = earley.find_routes(debug)
    if earley.is_valid_sentence():
        print '==> Sentence is valid.'
        trees = ParseTrees(routes, len(sentence), debug)
        print 'Valid parse trees:'
        print trees
    else:
        print '==> Sentence is invalid.'

if __name__ == '__main__':
    run()
