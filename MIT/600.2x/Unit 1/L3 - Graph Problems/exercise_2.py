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


# from graph_class import *

# nodes = []
# nodes.append(Node("ABCD")) # nodes[0]
# nodes.append(Node("ABDC")) # nodes[1]
# nodes.append(Node("ACBD")) # nodes[1]
# nodes.append(Node("ACDB")) # nodes[1]
# nodes.append(Node("ADBC")) # nodes[1]
# nodes.append(Node("ADCB")) # nodes[1]
# nodes.append(Node("BACD")) # nodes[2]
# nodes.append(Node("BADC")) # nodes[3]
# nodes.append(Node("BCAD")) # nodes[3]
# nodes.append(Node("BCDA")) # nodes[3]
# nodes.append(Node("BDAC")) # nodes[3]
# nodes.append(Node("BDCA")) # nodes[3]
# nodes.append(Node("CABD")) # nodes[4]
# nodes.append(Node("CADB")) # nodes[3]
# nodes.append(Node("CBAD")) # nodes[5]
# nodes.append(Node("CBDA")) # nodes[5]
# nodes.append(Node("CDAB")) # nodes[5]
# nodes.append(Node("CDBA")) # nodes[5]
# nodes.append(Node("DABC")) # nodes[4]
# nodes.append(Node("DACB")) # nodes[3]
# nodes.append(Node("DBAC")) # nodes[5]
# nodes.append(Node("DBCA")) # nodes[5]
# nodes.append(Node("DCAB")) # nodes[5]
# nodes.append(Node("DCBA")) # nodes[5]

# g = Graph()
# for n in nodes:
#     g.addNode(n)

# def createEdges(g):
#     for source_number in range(len(nodes)):
#         source = nodes[source_number].getName()
#         for dest_number in range(source_number+1, len(nodes)):
#             counter = 0
#             insert = True
#             dest = nodes[dest_number].getName()
#             for letter in ('A', 'B', 'C', 'D'):
#                 if source.index(letter) == dest.index(letter):
#                     counter += 1
#                 elif abs(source.index(letter) - dest.index(letter)) > 1:
#                     insert = False
#                     break
#             if counter == 2 and insert == True:
#                 g.addEdge(Edge(g.getNode(source), g.getNode(dest)))
#     return g

# print(createEdges(g))
