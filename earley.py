#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys
from grammar import *
from sentence import *
from parser import *

def print_trees(trees):
    for tree in trees:
        print tree


def run():
    if len(sys.argv)<3:
        print "Usage: earley.py <grammar.cfg> <sentence>"
        sys.exit(1)

    # load grammar from file, sentence from arguments
    grammar = Grammar.from_file(sys.argv[1])
    sentence = Sentence.from_string(sys.argv[2])

    # run parser
    earley = Parser(grammar, sentence)
    earley.parse()

    routes = earley.routes()
    # print results
    # print_trees(trees)

if __name__ == '__main__':
    run()
