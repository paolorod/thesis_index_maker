
from index_element import IndexElement

class ExtendedIndexElement(IndexElement):
    
    def __init__(self, index, entry, section_title, specification=None):
        self.section_title = section_title
        self.extended_entry = entry
        self.specification = specification
        IndexElement.__init__(self,section_title + "/" + entry + "/" + unicode(specification),index)
    
    def to_array(self):
        return [self.entry] + sorted(list(self.index))

    def __add__(self,other):
        if isinstance(other,ExtendedIndexElement):
            return ExtendedIndexElement(self.index | other.index,self.extended_entry,self.section_title,self.specification)
        else:
           return IndexElement.__add__(self,other)
                