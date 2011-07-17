def read_sentence(filename):
    "reads sentence from text file"
    # TODO move this out of here
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

    return sentence

