# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:49:49 2021

@author: Issamu Umeda
"""

from graph_class import *

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        
    def getWeight(self):
        return self.weight
        
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName() + ' (' + str(self.getWeight()) + ')'
        
g = buildCityGraph(Digraph)
t = WeightedEdge(g.getNode('Boston'), g.getNode('Providence'), 3)
print(t)
