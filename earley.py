#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

import sys
from grammar import *
from sentence import *
from parser import *
from parse_trees import *

def run():
    if len(sys.argv)<3:
        sys.stderr.write("Usage: earley.py <grammar.cfg> <sentence> [--debug]\n")
        sys.exit(1)

    # load grammar from file
    try:
        grammar = Grammar.from_file(sys.argv[1])
    except IOError as e:
        sys.stderr.write("Error reading file {0}\n".format(sys.argv[1]))
        sys.exit(1)

    # parse input sentence
    sentence = Sentence.from_string(sys.argv[2])

    # debug flag
    debug = len(sys.argv)==4 and sys.argv[3] == '--debug'

    # run parser
    earley = Parser(grammar, sentence, debug)
    earley.parse()

    # find and print validity, parse trees
    routes = earley.find_routes()
    if earley.is_valid_sentence():
        print '==> Sentence is valid.'

        trees = ParseTrees(routes, len(sentence))
        print 'Valid parse trees:'
        print trees
    else:
        print '==> Sentence is invalid.'

if __name__ == '__main__':
    run()
