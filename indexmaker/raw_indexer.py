from itertools import ifilter
from itertools import groupby
import re
import utils
import csv
import logging as log
import pattern.fr as pat
import stop_words
from index_element import *


def parse_and_split(doc_as_list):
    doc_index = list()
    for i in range(0,len(doc_as_list)-1):
        parsed = pat.parse(doc_as_list[i],lemmata=True,relations=True)
        for sentence in pat.split(parsed):
            for subject in sentence.subjects:
                doc_index += emit(subject,i)
            for objects in sentence.objects:
                doc_index += emit(objects,i)
    return doc_index

def emit(subsentence, i):
        final = []
        for x in subsentence:
            if x.string.lower() not in stop_words.StopWordsFr:
                if not x.pos[0] in 'C D E F I L P R S U W . : , ( )'.split():
                    if x.pos[0] in "J".split():
                        final.append(pat.predicative(x.string))
                    elif x.pos[0] == "V":
                        final.append(pat.conjugate(x.string, pat.INFINITIVE))
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
        entry =  u" ".join(final).strip()
        if entry=="": 
            return []
        else:
            return [IndexElement(entry.capitalize(), {i+1})]

