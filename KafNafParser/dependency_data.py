from lxml import etree
#from lxml.objectify import dump


class Cdependency:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('dep')
        else:
            self.node = node
            
    def get_node_comment(self):
        return self.node_comment
    
    def get_node(self):
        return self.node
    
    def get_from(self):
        return self.node.get('from')
    
    def get_to(self):
        return self.node.get('to')
    
    def get_function(self):
        return self.node.get('rfunc')

    def set_from(self, f):
        self.node.set('from',f)
    
    def set_to(self,t):
        self.node.set('to',t)
    
    def set_function(self,f):
        self.node.set('rfunc',f)
        

    def set_comment(self,c):
        c = c.replace('--','- -')
        self.node.insert(0,etree.Comment(c) )
            
    
    def __str__(self):
        return dump(self.node)



class Cdependencies:
    def __init__(self,node=None):
        if node is None:
            self.node = etree.Element('deps')
        else:
            self.node = node
            
    def get_node(self):
        return self.node
            
    def to_kaf(self):
        pass
    
    def to_naf(self):
        pass
            
    def __str__(self):
        return dump(self.node)


    def __get_node_deps(self):
        for node_dep in self.node.findall('dep'):
            yield node_dep
            
    def get_dependencies(self):
        for node in self.__get_node_deps():
            yield Cdependency(node)
            
            
    def add_dependency(self,my_dep):
        self.node.append(my_dep.get_node())
            