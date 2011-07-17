#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

# fix unicode for Python2.5
import sys, codecs
sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
reload(sys); sys.setdefaultencoding("utf-8")

if len(sys.argv)<2:
    print "Usage: read_cfg.py <grammar.cfg>"
    sys.exit(1)

filename = sys.argv[1]

try:
    lines = file(filename)
except IOError as e:
    sys.stderr.write("Error reading file {0}\n".format(filename))
    sys.exit(1)

grammar = {}
for line in lines:
    if line[0] == '#': # comment
        continue

    # head -> outcome | outcome | outcome
    rule = line.split('->')
    head = rule[0].strip()
    outcomes = [outcome.strip() for outcome in rule[1].split('|')]

    if head in grammar:
        grammar[head].extend(outcomes)
    else:
        grammar[head] = outcomes

print grammar
