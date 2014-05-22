# Modified for NAF KAF
from lxml import etree
from lxml.objectify import dump

class Cterm_sentiment:
    def __init__(self,node=None):
        self.type = 'NAF/KAF'
        if node is None:
            self.node = etree.Element('sentiment')
        else:
            self.node = node 
        #self.resource = self.polarity = self.strength = self.subjectivity = self.semantic_type = self.modifier = self.marker = self.product_feature = ''
        #if node is not None:
        #    self.resource = node.get('resource','')
        #    self.polarity = node.get('polarity','')
        #    self.strength = node.get('strength','')
        #    self.subjectivity = node.get('subjectivity','')
        #self.semantic_type = node.get('sentiment_semantic_type','')
        #    self.modifier = node.get('sentiment modifier','')
        #    self.marker = node.get('sentiment_marker','')
        #    self.product_feature = node.get('sentiment product feature','')
    
    def set_resource(self,r):
        self.node.set('resource',r)
    
    def get_node(self):
        return self.node
    
    def get_polarity(self):
        return self.node.get('polarity')
    
    def set_polarity(self,p):
        self.node.set('polarity',p)
    
    def get_modifier(self):
        return self.node.get('sentiment_modifier')
    
    def set_modifier(self,sm):
        self.node.set('sentiment_modifier',sm)

    def __str__(self):
        return dump(self.node)
