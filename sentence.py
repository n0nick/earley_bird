#!/usr/bin/python
# coding=utf-8
# -*- encoding: utf-8 -*-
import re

class Word:
    def __init__(self, word = '', tags = []):
        self.word = word
        self.tags = tags

    def __str__(self):
        return "{0}<{1}>".format(self.word, ','.join(self.tags))

    def is_tagged(self, tag):
        return tag in self.tags

class Sentence:
    def __init__(self, words = []):
        self.words = words

    def __str__(self):
        return ' '.join(str(w) for w in self.words)

    def __len__(self):
        return len(self.words)

    def __getitem__(self, item):
        if item >= 0 and item < len(self):
            return self.words[item]
        else:
            return None

    def add_word(self, word):
        self.words.append(word)

    @staticmethod
    def from_string(text):
        # prepare regular expressions to find word and tags
        lemmarex = re.compile('^[^\/]*')
        tagsrex = re.compile('\<([^\>]*)\>')

        sentence = Sentence()
        # time/time<N> flies/flies<N>/flies<V> like/like<P>/like<V> an/an<D> arrow/arrow<N>
        words = text.strip().split(' ')
        for word in words:
            lemma = lemmarex.match(word).group(0)
            tags = tagsrex.findall(word)
            w = Word(lemma, tags)
            sentence.add_word(w)

        return sentence

