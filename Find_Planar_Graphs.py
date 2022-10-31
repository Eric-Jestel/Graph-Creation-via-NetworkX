# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:24:01 2022

@author: Eric Jestel
"""

import networkx as nx

def generateAllGraphs():
    #Creates a empty graph on 8 vertices
    Root = nx.Graph()
    Root.add_nodes_from([x for x in range(0,8)])
    
    #Builds up a dictionary by mapping each key to an edge
    edgeDict = {}
    counter = 0
    for x in range(0,8):
        for y in range(x,8):
            #Blocks loops
            if x != y:
                edgeDict[counter] = (x,y)
                counter +=1
    
    #Initializes counter at the complete graph on 8 vertices. 2^28 +- 1
    counter = 268435456
    #Iterate until an answer is found
    while True:
        #Decrements counter
        counter -= 1
        #Builds up a graph based on the number. There are 28 possible edges, so a mapping can be 
        #made from 1 edge to 1 binary bit. If the bit is one, the edge is included, otherwise, it is not.
        #These binary bits can be converted to decimal to create a mapping between the integers and
        #all possible graphs on n vertices. 
        tempGraph = Root.copy()
        binForm = format(counter, '#0'+str(2+len(edgeDict))+'b')[2:]
        for position in range(len(edgeDict)):
            if binForm[position]=="1":
                tempGraph.add_edges_from([edgeDict[position]])
        #Creates the complement of the graph. This could also be done by taking the ones complement of
        #the binary number (substitute 0s for 1s and vice versa)
        compTemp = nx.complement(tempGraph)
        #Life check. Lets me know if the program has stalled and how fast it's going
        if counter%100000:
            print(counter)
        #Checks planarity of the graph and its complement. If both are planar, it returns the 
        #binary code of the graph
        if nx.is_planar(compTemp) and nx.is_planar(tempGraph):
            return binForm
        
#Draws graphs
def drawGraph(binaryCode):
    #Same as first function. Converts binary into graph
    tempGraph= nx.Graph()
    tempGraph.add_nodes_from([x for x in range(0,8)])
    edgeDict = {}
    counter = 0
    for x in range(0,8):
        for y in range(x,8):
            #Blocks loops
            if x != y:
                edgeDict[counter] = (x,y)
                counter +=1
    for position in range(len(edgeDict)):
        if binaryCode[position]=="1":
            tempGraph.add_edges_from([edgeDict[position]])
    #If graph is planar, draw it planar. Otherwise, draw it. Trying to draw a nonplanar graph as a 
    #planar graph gives an error.
    if nx.is_planar(tempGraph):
        nx.drawplanar(tempGraph)
    else:
        nx.draw(tempGraph)