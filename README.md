## Earley Bird

### An implementation of the Earley Parser in Python

Earley Bird is a small program that, given a well-formatted context-free grammar, and an input sentence that has already been passed through a part-of-speech tagger program, can tell you whether or not the sentence is valid in this grammar, and if so, output all possible parse trees in a nice format.

This program was written as a final project for a TAU seminar "Advanced Computational Linguistics" [0627.2223] taken at spring 2011.<br/>
It is based on the algorithm of [the Earley Parser](http://github.github.com/github-flavored-markdown/preview.html) as described on [Speech and Language Processing (Jurafsky, Martin)](http://www.cs.colorado.edu/~martin/slp2.html).<br/>
The input forms has been chosen and designed so the program would integrate with the [Apertium](http://apertium.org/) open-source machine translation framework.

### Usage

To run it, just call:<br/>
```python earley.py <grammar.cfg> <sentence> [--debug]```

See 'Input' for instructions on input formats.<br/>
Use ``--debug`` to get all kinds of secret messages during the process.

### Input

To use Earley Bird, one needs two things.

* __Context-free grammar:__  A set of production rules in the form of ``V -> w``, where ``V`` is a single nonterminal symbol, and ``w`` is a list of strings of terminals and/or nonterminals.<br/>
At least one rule with left-hand side ``S`` (for sentence) must exist in order for sentences to be valid.<br/>
An item in ``w`` can be empty, to represent epsilon productions.<br/>
For info, [see CFG description in Wikipedia](http://en.wikipedia.org/wiki/Context-free_grammar).<br/>
Earley bird reads a grammar from a text file where every line comprises of such rule. Comments are supported, prefixed by ``#``.<br/><br/>
Example:<br/>
<code>S -> NP VP | VP<br/>
NP -> D N | N | N NP<br/>
VP -> V | V NP | V PP | V NP PP<br/>
PP -> P NP
</code><br/><br/>
For other examples of CFG, see ``sample.cfg`` in the project directory.

* __Sentence:__ Earley Bird expects an input of a sentence string with words already parsed for possible parts of speech.<br/>
The input should be formatted using the [Apertium stream format](http://wiki.apertium.org/wiki/Apertium_stream_format), with each word followed by groups of a lemma and a list of tags, e.g.<br/>
```time/time<N> flies/fly<N>/fly<V> like/like<V>/like<P> an/a<D> arrow/arrow<N>```

### Output

The first line in the standard output would be the result of the validity check. i.e. either ```==> Sentence is valid.```, or ```==> Sentence is invalid.```

If the sentence was found invalid using the provided grammar, tough beans, that's it.

If it's valid, you'll also get a list of valid parse trees.<br/>
<code>==> Sentence is valid.<br/>
Valid parse trees:<br/>
<Parse Trees><br/>
Parse tree #1:<br/>
[.GAMMA [.S [.NP [.N [.time ] ] ] [.VP [.V [.flies ] ] [.PP [.P [.like ] ] [.NP [.D [.an ] ] [.N [.arrow ] ] ] ] ] ] ]<br/>
</Parse Trees></code>

Each tree is printed in the [Qtree format](http://www.ling.upenn.edu/advice/latex/qtree/), and you can then use several tools to use them in documents or generated images from them.<br/>
[phpSyntaxTree](http://www.ironcreek.net/phpsyntaxtree/) is a recommended tree image generation tool.

### License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

### Known Issues

1. Sentence input should be inside ``^...$`` to comply with the Apertium stream format.
1. There is a bug in creating the trees list in ParseTrees, causing all possible parse trees creates as branches of the same tree, instead of duplicating the head to different alternatives.
1. Some ambiguities are not represented, but this should be checked only after the trees creation is fixed.
1. Generated trees should be filtered and only ones that are long enough (as long as the sentence) should be returned.