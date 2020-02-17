
class IndexElement:

    def __init__(self, entry, index):
        self.entry = entry
        self.index = index
        return
    
    def __repr__(self):
        return "%s = %s" % (self.entry, self.index)
    
    def __eq__(self, other):
        return (self.entry, self.index) == (other.entry, other.index)

    def __hash__(self):
        return hash(repr(self))

    def to_array(self):
        return [self.entry] + sorted(list(self.index))

    def __add__(self,other):
        if not isinstance(other,IndexElement):
            raise Exception("Index Element instance expected")
        else:
            if(self.entry != other.entry):
                raise Exception("Only IndexElements with the same entry can be merged")
            else:
                return IndexElement(self.entry,self.index | other.index)

    def __iadd__(self, other):
        if not isinstance(other,IndexElement):
            raise Exception("Index Element instance expected")
        else:
            if(self.entry != other.entry):
                raise Exception("Only IndexElements with the same entry can be merged")
            else:
                self.index |= other.index
    
    def add_index(self,index_value):
        self.index.add(index_value)