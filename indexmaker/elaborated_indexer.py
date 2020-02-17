
from extended_index_element import *
import logging
import utils
import yaml

import lemmatizer as lem

log = logging.getLogger()

def parse_yaml(index_structure_yaml):
    log.info("Loading structure file %s",index_structure_yaml)
    with open(index_structure_yaml) as f:
        yaml_raw_structure = yaml.load(f)
        index_structure = utils.nested_dict(3,list)
        for section in yaml_raw_structure:
            section_title = section.keys()[0]
            section_content = section[section_title]
            # in case is empty, manage it as it has the section title as entry
            if section_content is None:
                section_content = [section_title]
            # elaborate section content
            for element in section_content:
                # manage and uniform sub-labels
                if isinstance(element, basestring):
                    word = element
                    specifications = [None]
                elif isinstance(element, dict):
                    word = element.keys()[0]
                    specifications = [None] + element[word]
                else:
                    log.warn("Element "+str(element)+"Ignored - type:"+type(element))
                for spec in specifications:
                    index_structure[section_title][word][spec] = []
        return index_structure

def parse_and_split(index_structure,doc_as_list):
    log.info("Starting Index Extraction")
    doc_index = list()
    length = len(doc_as_list)-1
    utils.printProgressBar(0, length-1, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i in range(0,length):
        doc_index += check_and_emit(index_structure,doc_as_list[i],i)
        utils.printProgressBar(i, length-1, prefix = 'Progress:', suffix = 'Complete', length = 50)
    return doc_index

def check_and_emit(index_structure,paragraph,i):
    local_index = list()
    for section_title in index_structure.keys():
        for word in index_structure[section_title]:
                for spec in index_structure[section_title][word]:
                    local_index += emit_if_present(paragraph,i,section_title,word,spec)      
    return local_index

def emit_if_present(paragraph,i,section_title,entry,specification):
    words = [entry]
    if specification is not None:
       words.append(specification)
    if all([match(word,paragraph) for word in words]):
        return [ExtendedIndexElement({i+1},entry,section_title,specification)]
    else: 
        return []

def match(word,paragraph):
    return lem.lemmatise(word.lower()) in lem.lemmatise(paragraph).lower()

def index_printer(index_structure,consolidated_index):
    log.info('Printing Structured Index')
    dict_index = index_structure.copy()

    for element in consolidated_index:
        dict_index[element.section_title][element.extended_entry][element.specification] = sorted(element.index)
    
    out = u""
    section_keys = dict_index.keys()
    section_keys.sort()
    for section_title in section_keys:
        out +=  " %s:\n" % (section_title)
        words_keys = dict_index[section_title].keys()
        words_keys.sort()
        for word in words_keys:
            out +=  "   %s: %s\n" % (word,page_list_as_string(dict_index[section_title][word][None]))
            #out +=  "   %s:\n" % (word)
            for specification in dict_index[section_title][word].keys():
                if specification is not None:
                    out +=  "       %s: %s\n" % (specification,page_list_as_string(dict_index[section_title][word][specification]))
        out += "\n"
    return out
    

def page_list_as_string(pagelist):
    return ",".join(map(lambda x:str(x), pagelist))
