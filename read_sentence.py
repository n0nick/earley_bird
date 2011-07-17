#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-

# fix unicode for Python2.5
import sys, codecs, re
sys.stdin  = codecs.getreader('utf-8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)
reload(sys); sys.setdefaultencoding("utf-8")

if len(sys.argv)<2:
    print "Usage: read_sentence.py <sentence.txt>"
    sys.exit(1)

filename = sys.argv[1]

try:
    lines = file(filename)
except IOError as e:
    sys.stderr.write("Error reading file {0}\n".format(filename))
    sys.exit(1)

# prepare regular expressions to find word and tags
lemmarex = re.compile('^[^\/]*')
tagsrex = re.compile('\<([^\>]*)\>')

sentence = []
for line in lines:
    if line[0] == '#': # comment
        continue

    # time/time<N> flies/flies<N>/flies<V> like/like<P>/like<V> an/an<D> arrow/arrow<N>
    words = line.strip().split(' ')
    for word in words:
        lemma = lemmarex.match(word).group(0)
        tags = tagsrex.findall(word)
        sentence.append((lemma, tags))

print sentence
