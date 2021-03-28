# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 21:54:11 2021

@author: Issamu Umeda
"""
from graph_class import *

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

def createEdges(g):
    for source_number in range(len(nodes)):
        source = nodes[source_number].getName()
        for dest_number in range(source_number+1, len(nodes)):
            dest = nodes[dest_number].getName()
            for letter in ('A', 'B', 'C'):
                if source.index(letter) == dest.index(letter) and source.index(letter) != 1:
                    g.addEdge(Edge(g.getNode(source), g.getNode(dest)))
    return g
        
print(createEdges(g))
