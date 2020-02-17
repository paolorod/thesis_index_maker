import pattern.fr as pat
import stop_words

lemmatised_cache = dict()

def lemmatise(string):
    if lemmatised_cache.has_key(string):
        return lemmatised_cache.get(string)
    else:
        text = pat.split(pat.parse(string))
        final = []
        for subsentence in text:
            for x in subsentence:
                if x.string.lower() not in stop_words.StopWordsFr:
                    if not x.pos[0] in 'C I P U L . : , ( )'.split():
                        if x.pos[0] in "J".split():
                            final.append(pat.predicative(x.string))
                        #elif x.pos[0] == "V":
                        #    final.append(pat.conjugate(x.string, pat.INFINITIVE))
                        elif x.pos == 'NNS' and x.string[-1] == u"s" and x.string.lower() not in stop_words.ListeS:
                            final.append(pat.singularize(x.string))
                        elif x.pos == 'NNS' and x.string[-4:] == u"eaux":
                            final.append(pat.singularize(x.string))
                        elif x.pos == 'NNS' and x.string[-3:] == u"aux":
                            final.append(x.string[:-2]+u'l')
                        else:
                            final.append(x.string)
                else:
                    continue
        entry =  " ".join(final).strip()
        lemmatised_cache[string] = entry
        return entry